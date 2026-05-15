from sys import argv
from PIL import Image


def main():
    watermark = Image.open("assets/watermark.png")

    for arg in argv[1:]:
        print(f"Converting '{arg}', ", end="")
        image = Image.open(arg)

        shrink = 10

        # Resize with constant width
        # watermark_size = (
        #     image.size[0] // 10,
        #     (image.size[0] // 10) // (watermark.size[0] // watermark.size[1]),
        # )

        # Resize with constant height
        watermark_size = (
            (image.size[1] // shrink) * (watermark.size[0] // watermark.size[1]),
            image.size[1] // shrink,
        )
        watermark = watermark.resize(watermark_size)

        watermark_pos = (0, image.size[1] - watermark_size[1])

        output = Image.new("RGBA", image.size)
        output.paste(image, (0, 0))
        output.paste(watermark, watermark_pos, mask=watermark)
        output = output.convert("RGB")

        output.save(arg)
        print("done!")


if __name__ == "__main__":
    main()
