from PIL import Image
import myapi.db.ResultPerimetryService as PRS
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.interpolate import griddata
from io import BytesIO
from matplotlib.colors import LinearSegmentedColormap


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
        
        combined_image = ImageCreator.add_colorbar(combined_image)
        
        return combined_image
    
    @staticmethod
    def add_colorbar(image):
        """
        Fügt eine Farbskala (Colorbar) mittig unter dem Bild hinzu.

        Args:
            image (Image): Das kombinierte Bild ohne Farbskala.

        Returns:
            Image: Das Bild mit der Farbskala mittig darunter.
        """
        # Erstelle eine Farbskala
        fig, ax = plt.subplots(figsize=(image.width / 100, 1))  # Breite an Bild anpassen
        fig.subplots_adjust(bottom=0.5)

        # Colormap definieren
        colors = [(1, 1, 1), (0.2, 0.2, 0.2)]  # Von Grau zu Weiß
        custom_cmap = LinearSegmentedColormap.from_list("custom_greys", colors)
        color_data = np.linspace(0, 1, 256).reshape(1, -1)
        ax.imshow(color_data, cmap=custom_cmap, aspect='auto')

        # Beschriftung der Farbskala
        ax.set_xticks([0, 255])
        ax.set_xticklabels(['gesehen', 'nicht gesehen'], fontsize=14)
        ax.set_yticks([])

        # Farbskala in Puffer speichern
        buffer = BytesIO()
        plt.savefig(buffer, format='png', bbox_inches='tight', pad_inches=0.2)
        plt.close()
        buffer.seek(0)

        # Farbskala in PIL.Image umwandeln
        colorbar_image = Image.open(buffer)

        # Neue Bildgröße definieren
        new_height = image.height + colorbar_image.height

        # Neues Bild erstellen und die beiden Bilder kombinieren
        combined_image = Image.new("RGB", (image.width, new_height), "white")
        combined_image.paste(image, (0, 0))  # Originalbild oben
        combined_image.paste(colorbar_image, (((image.width - colorbar_image.width) // 2) + 11, image.height))

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
        
        colors = [(1, 1, 1), (0.2, 0.2, 0.2)]  # Von Grau zu Weiß (RGB)
        custom_cmap = LinearSegmentedColormap.from_list("custom_greys", colors)

        plt.figure(figsize=(10, 10))
        plt.imshow(grid_z, extent=(min(x), max(x), min(y), max(y)), origin='lower',
                   cmap=custom_cmap, aspect='equal')
        #plt.colorbar(label='Sichtbarkeit (0 = gesehen, 1 = nicht gesehen)', orientation='horizontal')
        plt.axis('off')
        plt.axhline(50, color='black', linewidth=2, linestyle="--")  # Horizontale Linie durch (0, 0)
        plt.axvline(50, color='black', linewidth=2,  linestyle="--")
        plt.scatter(x, y, color="white", edgecolor='k')

        buffer = BytesIO()
        plt.savefig(buffer, format='png', bbox_inches='tight', pad_inches=0.1)
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
 
        
            
    
   