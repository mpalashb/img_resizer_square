from PIL import Image

img_v2 = "img_fname.jpg"


def img_resize(img_name):

    img = Image.open(img_name).convert('RGB')
    # Extract the pixel color

    # grabing the middle of top (middle x and o or top y)
    topmost_color = img.getpixel((img.width // 2, 0))
    # grabing the middle of left (0 of x and middle or left y)
    leftmost_color = img.getpixel((0, img.height // 2))
    # grabing the middle of right (o of x right and middle y)
    rightmost_color = img.getpixel((img.width - 1, img.height // 2))
    # grabing the middle of buttom (middle of x and o or buttom y)
    bottommost_color = img.getpixel((img.width // 2, img.height - 1))

    width, height = img.size
    new_max_width_or_height = max(width, height)

    if width > height:
        # to divided to both of left and right
        border_height = (new_max_width_or_height - height)//2

        border_top = Image.new(
            'RGB', (width, border_height), topmost_color)
        border_bottom = Image.new(
            'RGB', (width, border_height), bottommost_color)

        # Create a new image with borders on the top and bottom
        # creating a blank square size of required
        image_with_borders = Image.new(
            'RGB', (width, height + border_height * 2))
        # inserting top border with color into image_with_borders for blank with required size
        image_with_borders.paste(border_top, (0, 0))
        # inserting orginal image with existing size into image_with_borders for blank with required size
        image_with_borders.paste(img, (0, border_height))
        # inserting buttom border with color into image_with_borders for blank with required size
        image_with_borders.paste(
            border_bottom, (0, height + border_height))

        # Save the manipulated image
        image_with_borders.save('resized_with_borders_'+img_name)

    else:
        # to divided to both of left and right
        border_width = (new_max_width_or_height - width)//2

        border_left = Image.new(
            'RGB', (border_width, height), leftmost_color)
        border_right = Image.new(
            'RGB', (border_width, height), rightmost_color)

        # Create a new image with borders on the top and bottom
        # creating a blank square size of required
        image_with_borders = Image.new(
            'RGB', (width + border_width * 2, height))
        # inserting top border with color into image_with_borders for blank with required size
        image_with_borders.paste(border_left, (0, 0))
        # inserting orginal image with existing size into image_with_borders for blank with required size
        image_with_borders.paste(img, (border_width, 0))
        # inserting buttom border with color into image_with_borders for blank with required size
        image_with_borders.paste(
            border_right, (width + border_width, 0))

        # Save the manipulated image
        image_with_borders.save('2resized_with_borders_'+img_name)


img_resize(img_v2)
