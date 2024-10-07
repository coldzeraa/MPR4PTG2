from PIL import Image, ImageDraw, ImageFont
import myapi.db.PointResultService as PRS

class ImageCreator:
    
    @staticmethod
    def createImage(exID):
        pointResults = PRS.PointResultService.getByExID(exID)
        
        leftImage = ImageCreator.drawPoints(ImageCreator.splitArrayInHalf(pointResults)[0])
        rightImage = ImageCreator.drawPoints(ImageCreator.splitArrayInHalf(pointResults)[1])
        
        combined_width = leftImage.width + rightImage.width
        combined_height = max(leftImage.height, rightImage.height)
        combined_image = Image.new('RGB', (combined_width, combined_height))
        combined_image.paste(leftImage, (0, 0))
        combined_image.paste(rightImage, (leftImage.width, 0))
        
        return combined_image
        
           
            
    @staticmethod
    def drawPoints(currentPointResult):
        
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
    def splitArrayInHalf(array):
        mid = len(array) // 2
        first_half = array[:mid]
        second_half = array[mid:]
        return first_half, second_half
        
            
    
   