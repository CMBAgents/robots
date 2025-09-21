from PIL import Image, ImageDraw

# --- Settings ---
scale = 16
px = 16
out_size = px * scale

# Color palettes
COLOR_PALETTES = {
    'orange': {
        'ACCENT': (255, 160, 80, 255),
        'HELMET': (180, 175, 205, 255),
        'HELMET_DK': (140, 135, 160, 255),
        'HELMET_LT': (210, 205, 230, 255),
        'EAR_DK': (110, 105, 130, 255)
    },
    'blue': {
        'ACCENT': (80, 160, 255, 255),
        'HELMET': (175, 205, 230, 255),
        'HELMET_DK': (135, 160, 190, 255),
        'HELMET_LT': (205, 230, 255, 255),
        'EAR_DK': (105, 130, 160, 255)
    },
    'green': {
        'ACCENT': (80, 255, 160, 255),
        'HELMET': (175, 230, 205, 255),
        'HELMET_DK': (135, 190, 160, 255),
        'HELMET_LT': (205, 255, 230, 255),
        'EAR_DK': (105, 160, 130, 255)
    },
    'red': {
        'ACCENT': (255, 80, 80, 255),
        'HELMET': (230, 175, 175, 255),
        'HELMET_DK': (190, 135, 135, 255),
        'HELMET_LT': (255, 205, 205, 255),
        'EAR_DK': (160, 105, 105, 255)
    }
}

# Base colors
BG = (0, 0, 0, 0)   # transparent
FACE = (5, 5, 10, 255)

def generate_robot(color_name):
    """Generate a robot with the specified color scheme"""
    if color_name not in COLOR_PALETTES:
        raise ValueError(f"Color '{color_name}' not supported. Available: {list(COLOR_PALETTES.keys())}")
    
    colors = COLOR_PALETTES[color_name]
    
    # Create transparent base
    img = Image.new("RGBA", (px, px), BG)
    d = ImageDraw.Draw(img)

    def box(x0, y0, x1, y1, fill):
        d.rectangle([x0, y0, x1, y1], fill=fill)

    # --- draw robot ---
    # Helmet (thin edges)
    box(2, 4, 13, 5, colors['HELMET'])
    box(3, 3, 12, 3, colors['HELMET_LT'])
    box(1, 6, 2, 12, colors['HELMET_DK'])
    box(13, 6, 14, 12, colors['HELMET_DK'])
    box(3, 12, 12, 13, colors['HELMET'])
    box(3, 6, 12, 11, colors['HELMET'])

    # Ears
    box(0, 8, 1, 10, colors['EAR_DK'])
    box(14, 8, 15, 10, colors['EAR_DK'])

    # Face screen
    box(3, 6, 12, 11, FACE)

    # Eyes (moved up one pixel)
    box(5, 7, 6, 7, colors['HELMET_LT'])
    box(9, 7, 10, 7, colors['HELMET_LT'])

    # Frown (symmetrical like /--\)
    box(5, 10, 5, 10, colors['ACCENT'])       # left edge down
    box(6, 9, 9, 9, colors['ACCENT'])       # center up
    box(10, 10, 10, 10, colors['ACCENT'])      # right edge down

    # Antenna
    box(7, 2, 8, 2, colors['HELMET_DK'])
    box(7, 1, 8, 1, colors['HELMET'])
    box(7, 0, 8, 0, colors['ACCENT'])

    # --- Upscale with transparency ---
    out = img.resize((out_size, out_size), resample=Image.NEAREST)
    
    # Save with color-specific filename
    filename = f"robot_sad_{color_name}.png"
    out.save(filename, "PNG")
    print(f"Generated {color_name} robot: {filename}")
    
    return out

# Generate all color variants
if __name__ == "__main__":
    for color in COLOR_PALETTES.keys():
        generate_robot(color)