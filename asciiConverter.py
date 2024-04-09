from PIL import Image

class AsciiConverter:
  #image as a string of file location, scale of image
  def asciiConvert(image, scale):
    grid = []

    #image to be opened, then resized based on scale
    img = Image.open(image)
    w , h = img.size
    w = int(w * scale)
    h = int(h * scale)
    img = img.resize((w , h))
    pixel_values = img.load()
    for y in range(int(h)):
      grid.append(["X"] * w)

    #file writer to write ascii
    f = open("art.txt", "w+")

    #setting grid values
    for y in range(int(h)):
      for x in range(int(w)):
        if(sum(pixel_values[x,y]) <= 48.4):
          grid[y][x] == '@'
        elif(48.4 < sum(pixel_values[x,y]) <= 96.8):
          grid[y][x] = '#'
        elif(96.8 < sum(pixel_values[x,y]) <= 145.2):
          grid[y][x] = 'b'
        elif(145.2 < sum(pixel_values[x,y]) <= 194):
          grid[y][x] = 'p'
        elif(194 < sum(pixel_values[x,y]) <= 242.4):
          grid[y][x] = 'w'
        elif(242.4 < sum(pixel_values[x,y]) <= 290.8):
          grid[y][x] = '0'
        elif(290.8 < sum(pixel_values[x,y]) <= 339.6):
          grid[y][x] = 'C'
        elif(339.6 < sum(pixel_values[x,y]) <= 388):
          grid[y][x] = 'X'
        elif(388 < sum(pixel_values[x,y]) <= 436.4):
          grid[y][x] = 'u'
        elif(436.4 < sum(pixel_values[x,y]) <= 484):
          grid[y][x] = 'j'
        elif(484 < sum(pixel_values[x,y]) <= 532.4):
          grid[y][x] = '\\'
        elif(532.4 < sum(pixel_values[x,y]) <= 580.8):
          grid[y][x] = '{'
        elif(580.8 < sum(pixel_values[x,y]) <= 629.2):
          grid[y][x] = '?'
        elif(629.2 < sum(pixel_values[x,y]) <= 678):
          grid[y][x] = '!'
        else:
          grid[y][x] = '^'
        
        f.write(grid[y][x])
      f.write("\n")
  
  asciiConvert("donuts3.png", .5)
    


  