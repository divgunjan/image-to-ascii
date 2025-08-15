# **ASCII ART CONVERTER**

Transform any image into stunning ASCII art with this powerful Python-based converter. Create both terminal-friendly text output and beautifully colored ASCII images. Whether you're looking to create retro terminal displays, add artistic flair to your projects, or simply explore the beauty of text-based graphics, this tool delivers exceptional results with fine-tuned control over every aspect of the conversion process.


|   |   |
|:--:|:--:|
| ![Original](https://images2.imgbox.com/7f/23/LZBKeOAK_o.jpg) | ![ASCII Art](https://images2.imgbox.com/9f/55/yfxxm6Fx_o.png) |
---

## **🚀 QUICK START**

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/ascii-art-converter.git
cd ascii-art-converter

# Install required dependencies
pip install -r requirements.txt
```

### Basic Usage

```bash
# Convert an image to ASCII art
python ascii_converter.py input_image.jpg

# Save output to file
python ascii_converter.py input_image.jpg --output ascii_art.txt

# Quick preview in terminal
python ascii_converter.py input_image.jpg --preview
```

---

## **📋 DEPENDENCIES**

```
Pillow>=9.0.0
```

---

## **⚙️ CUSTOMIZATION**

### Key Parameters (modify in the script)

| Parameter | Current Value | Description |
|-----------|---------------|-------------|
| `new_width` | `150` | Output width in characters |
| `aspect_ratio` | `0.85` | Height adjustment factor |
| `contrast_enhance` | `1.5` | Contrast enhancement multiplier |
| `ascii_chars` | `"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1[]?-_+~<>i!lI;:,'."`| Character set (dark to light) |
| `dark_threshold` | `25` | Brightness below which pixels become blank |
| `dominant_threshold` | `30` | Distance threshold for dominant color detection |

### How to Customize

1. **Change Input Image**: Modify the filename in this line:
   ```python
   img = Image.open("images/1_test.jpg")  # Change to your image
   ```

2. **Adjust Resolution**: Modify `new_width` for different sizes:
   ```python
   new_width = 100  # Smaller for compact art
   new_width = 200  # Larger for detailed art
   ```

3. **Fine-tune Contrast**: Adjust the enhancement value:
   ```python
   image = ImageEnhance.Contrast(image).enhance(2.0)  # Higher contrast
   ```

4. **Customize Character Set**: Use different symbols:
   ```python
   ascii_chars = "█▓▒░ "  # Block characters
   ascii_chars = "@#%*+=-:. "  # Classic set
   ```

---

## **🔧 HOW IT WORKS**

### The Conversion Process

1. **Image Loading & Preprocessing**
   - Load image using PIL (Python Imaging Library)
   - Resize to target dimensions while maintaining aspect ratio
   - Apply contrast enhancement for better definition

2. **Color Analysis**
   - Calculate pixel brightness using luminance formula: `0.299*R + 0.587*G + 0.114*B`
   - Identify dominant color using pixel frequency analysis
   - Measure color distance for dominant color detection

3. **Smart Character Mapping**
   - **Dark areas** (brightness < 25): Rendered as blank spaces
   - **Dominant color regions**: Represented with dots (`.`) 
   - **Other areas**: Mapped to ASCII characters based on brightness
   - Characters range from dark (`$@B%`) to light (`:,'."`)

4. **Colored Output Generation**
   - Create new image with calculated dimensions
   - Draw each ASCII character with its original pixel color
   - Export as PNG with full color preservation

### Character Density Scale

```
Darkest → Lightest
$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1[]?-_+~<>i!lI;:,'.
```

### Unique Features

- **Dominant Color Detection**: Automatically identifies and highlights the most common color
- **Smart Blank Handling**: Very dark areas become transparent for better contrast
- **Color Preservation**: Each character retains the original pixel's color information

---

## **🎨 OPTIMIZATION GUIDE**

### For Different Image Types

**High Contrast Images (Logos, Text)**
```python
new_width = 120
image = ImageEnhance.Contrast(image).enhance(2.0)
dark_threshold = 30
```

**Photographs & Complex Images**
```python
new_width = 100
image = ImageEnhance.Contrast(image).enhance(1.2)
dominant_threshold = 40
```

**Artistic/Stylized Output**
```python
ascii_chars = "█▓▒░ "  # Block style
new_width = 80
```

### Fine-Tuning Tips

- **Resolution**: Start with 100-150 width for balanced detail
- **Contrast**: Increase (1.8-2.5) for sharper definition, decrease (1.0-1.3) for softer gradients
- **Dark Threshold**: Lower values (15-20) show more detail in shadows
- **Dominant Threshold**: Higher values (40-50) reduce dominant color influence

### Sample Images Included

- `images/1_test.jpg` - Default test image
- `images/adams.jpg` - Portrait example  
- `images/doom.jpg` - High contrast logo
- `colored_ascii.png` - Generated output example

---

## **📁 PROJECT STRUCTURE**

```
ascii-art-converter/
├── images/
│   ├── 1_test.jpg        # Default test image
│   ├── adams.jpg         # Portrait sample
│   └── doom.jpg          # Logo sample
├── pillolib.py          # Main conversion script
├── LICENSE # LICENSE
├── colored_ascii.png     # Generated output example
└── README.md             # This file
```

---

## **🧪 TESTING**

Try the converter with different images:

```bash
# Run with default test image
python pillolib.py

# Test with different samples (modify script to change input)
# - images/adams.jpg for portrait testing
# - images/doom.jpg for high-contrast logos
# - Your own images in the images/ folder
```

The script will output the dominant color found and save the result as `colored_ascii.png`.

---

<!--## **🤝 CONTRIBUTING**

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on:

- Submitting bug reports
- Proposing new features
- Code style guidelines
- Pull request process

---

## **📄 LICENSE**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **🙏 ACKNOWLEDGMENTS**

- Inspired by the classic ASCII art movement
- Built with Python's PIL library
- Thanks to the open-source community for continuous inspiration

---` 

## **📞 SUPPORT**

- **Issues**: [GitHub Issues](https://github.com/your-username/ascii-art-converter/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-username/ascii-art-converter/discussions)
- **Email**: your-email@example.com

--- -->

*Transform your digital world into the timeless art of ASCII. Every pixel tells a story.* ✨
