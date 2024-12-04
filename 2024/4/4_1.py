class Grid:
    def __init__(self, width, height, values):
        self.width = width
        self.height = height
        if width * height == len(values):
            self.values = values
        else:
            raise ValueError("This grid is not coherent")
    
    def get(self, x, y):
        if x < self.width and y < self.height:
            return self.values[x + y * self.width]
        else:
            raise ValueError("This is outside the grid")
            
    # Get ONE word from a coordinate with a direction. Return "" if out of bound
    def get_word(self, start_x, start_y, length, x_direction, y_direction):
        # Start out of bound
        if start_x >= self.width:
            return ""
        # Start out of bound
        elif start_y >= self.height:
            return ""
        # End out of bound
        elif not (0 <= start_x + (length-1) * x_direction < self.width):
            return ""
        # End out of bound
        elif not (0 <= start_y + (length-1) * y_direction < self.height):
            return ""
        else:
            letters = []
            for i in range(length):
                letters.append(self.get(start_x + i * x_direction , start_y + i * y_direction))
            return "".join(letters)

    # Get ALL words from a coordinate. (Max 8, 8 directions)
    def get_coordinate_words(self, start_x, start_y, length):
        word_list = []
        word_list.append(self.get_word(start_x ,start_y ,length,1,0))
        word_list.append(self.get_word(start_x ,start_y ,length,0,1))
        word_list.append(self.get_word(start_x ,start_y ,length,-1,0))
        word_list.append(self.get_word(start_x ,start_y ,length,0,-1))
        word_list.append(self.get_word(start_x ,start_y ,length,1,1))
        word_list.append(self.get_word(start_x ,start_y ,length,1,-1))
        word_list.append(self.get_word(start_x ,start_y ,length,-1,1))
        word_list.append(self.get_word(start_x ,start_y ,length,-1,-1))
        return [word for word in word_list if word != "" ]
    
    # Get ALL words from the grid
    def get_grid_words(self,length):
        word_list = []
        for x in range(width):
            for y in range(height):
                word_list.extend(self.get_coordinate_words(x,y,length))
        return word_list
    
    # Count occurence of a specific word
    def count_all_occurences(self,word):
        length = len(word)
        word_list = self.get_grid_words(length)
        return word_list.count(word)

values = []
width = 0
height = 0
with open("2024/4/input.txt", mode="r") as file:
    for line in file:
        clean_line = line.strip()
        values.extend(list(clean_line))
        height += 1
        width = max(width,len(clean_line))
grid = Grid(width, height, values)
print(grid.count_all_occurences('XMAS'))
