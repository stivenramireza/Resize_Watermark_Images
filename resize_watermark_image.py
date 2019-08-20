from PIL import Image

def create_watermark(image_path, final_image_path, watermark):
    main = Image.open(image_path)
    mark = Image.open(watermark)

    mask = mark.convert('L').point(lambda x: min(x, 25))
    mark.putalpha(mask)

    mark_width, mark_height = mark.size
    main_width, main_height = main.size
    aspect_ratio = mark_width / mark_height
    new_mark_width = main_width * 1
    mark.thumbnail((new_mark_width, new_mark_width / aspect_ratio), Image.ANTIALIAS)

    tmp_img = Image.new('RGB', main.size)

    for i in range(0, tmp_img.size[0], mark.size[0]):
        for j in range(0, tmp_img.size[1], mark.size[1]):
            main.paste(mark, (i, j), mark)
            main.thumbnail((8000, 8000), Image.ANTIALIAS)
            main.save(final_image_path, quality=100)

if __name__ == '__main__':
<<<<<<< HEAD
    create_watermark('images/original/2.JPG',
                     'images/generated_image.jpg',
                     'images/watermark/logo2000.png')
=======
    create_watermark('images/original.jpg',
                     'images/original_final_watermarked.jpg',
                     'images/pybites_trans.png')
>>>>>>> df49a21218400198078ac65f53cc619be5afd87b
