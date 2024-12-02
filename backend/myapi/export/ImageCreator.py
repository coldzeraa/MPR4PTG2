from PIL import Image
import myapi.db.ResultPerimetryService as PRS
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.interpolate import griddata
from io import BytesIO


class ImageCreator:
    
    @staticmethod
    def create_image(exID):
        """
            Creates image with all points for given examination
            Args:
                exID: ID of affected examination

            Returns:
                Image: created image
        """
        pointResults = PRS.ResultPerimetryService.getByExID(exID)
        
        pointResultsArr = []
        matplotlib.use('Agg')
        for pr in pointResults:
            pointResultsArr.append([pr.p.x, pr.p.y, 0 if pr.seen else 1])
                
        pointsLeftImage, pointsRightImage = ImageCreator.split_array_in_half(pointResultsArr)
        
        rightImage = ImageCreator.draw_points(pointsRightImage)
        leftImage = ImageCreator.draw_points(pointsLeftImage)
        
        combined_width = leftImage.width + rightImage.width
        combined_height = max(leftImage.height, rightImage.height)
        combined_image = Image.new('RGB', (combined_width, combined_height))
        combined_image.paste(leftImage, (0, 0))
        combined_image.paste(rightImage, (leftImage.width, 0))
        
        return combined_image

    @staticmethod
    def draw_points(currentPointResult):
        """Draws points from array to Image

            Args:
                currentPointResult array: array with point results

            Returns:
                Image: Image with drawn points
        """
        
        pointResultsArr = np.array(currentPointResult)
        
        x, y, seen = pointResultsArr[:, 0], pointResultsArr[:, 1], pointResultsArr[:, 2]
        
        grid_x, grid_y = np.meshgrid(np.linspace(min(x), max(x), 500),
                                np.linspace(min(y), max(y), 500))

        grid_z = griddata((x, y), seen, (grid_x, grid_y), method='linear')

        plt.imshow(grid_z, extent=(min(x), max(x), min(y), max(y)), origin='lower',
                   cmap='Greys', aspect='auto')
        plt.colorbar(label='Sichtbarkeit (0 = gesehen, 1 = nicht gesehen)')
        plt.scatter(x, y, color="white", edgecolor='k')
        plt.xlabel('X-Koordinate')
        plt.ylabel('Y-Koordinate')
        plt.tight_layout()

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        plt.close()
        buffer.seek(0)
        img = Image.open(buffer).copy()
        buffer.close()
        return img

    @staticmethod
    def split_array_in_half(array):
        """
            Splits the given array in two

        Args:
            array: array to split

        Returns:
            two arrays first half and second half
        """
        mid = len(array) // 2
        return array[:mid], array[mid:]
 
        
            
    
   