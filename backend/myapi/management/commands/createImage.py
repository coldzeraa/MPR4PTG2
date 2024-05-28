from django.core.management.base import BaseCommand
from PIL import Image, ImageDraw, ImageFont

import myapi.db.PointResultService as PRS


class Command(BaseCommand):

    def handle(self, *args, **options):
        pointResults = PRS.PointResultService.get_all()
        width, height = 102, 102
        image = Image.new('RGB', (width, height), color = 'white')
        draw = ImageDraw.Draw(image)

        for pRes in pointResults:

            point = pRes.p
            seen = pRes.seen
            pos = (point.x + 2, point.y + 2)

            if seen:
                draw.point(pos, fill="green")
            else:
                draw.point(pos, fill="red")

        image.save('result.png')