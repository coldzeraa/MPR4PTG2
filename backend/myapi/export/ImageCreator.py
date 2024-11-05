from PIL import Image, ImageDraw, ImageFont
import myapi.db.ResultPerimetryService as PRS

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
        pointResults = PRS.PointResultService.getByExID(exID)
        
        leftImage = ImageCreator.draw_points(ImageCreator.split_array_in_half(pointResults)[0])
        rightImage = ImageCreator.draw_points(ImageCreator.split_array_in_half(pointResults)[1])
        
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
        
        width, height = 102, 102
        
        image = Image.new('RGB', (width, height), color = 'white')
        draw = ImageDraw.Draw(image)
        
        for pRes in currentPointResult:
            point = pRes.p
            seen = pRes.seen
            pos = ((point.x + 2), (point.y + 2))

            if seen:
                draw.point(pos, fill="green")
            else:
                draw.point(pos, fill="red")
                
            draw.rectangle([0, 0, width-1, height-1], outline="black")
            
        return image

        
        
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
        first_half = array[:mid]
        second_half = array[mid:]
        return first_half, second_half
        
            
    
   