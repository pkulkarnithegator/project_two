def get_escape_time(c:complex, max_iterations:int) -> int | None:
  """
  Returns the number of iterations before the complex number following the
  Mandelbrot sequence exceeds a magnitude of 2

  Input: c for starting complex number, and max_iterations determining number of steps until to stop
  Output: int value for number of iterations until complex number magnituded is greater than 2 or
            None if magnitude is lower or equal to 2 even after completing max_iterations
  """
  z=c
  if abs(z) > 2:
    return 0
  for i in range(max_iterations):
    z=z**2 + c
    if abs(z) > 2:
      return i+1
  return None
  
def get_complex_grid(top_left:complex, bottom_right:complex, step:float) -> np.ndarray:
  """returns a grid of complex numbers as coordinates, each by a distance of [step]

  input: top_left which is the "beginning" complex number that will located in the top left corner
         bottom_right: which is a complex that specifies the end points of the grid laterally and longitudinally
         step: which is an int that indicates the length of a unit within the grid
  output: an ndarray with complex numbers distanced by a specific distance (step)"""
  width_dist = bottom_right.real - top_left.real
  height_dist = top_left.imag - bottom_right.imag

  width = int(width_dist // step)
  height = int(height_dist // step)

  width_side = np.arange(0,width*step+step, step)
  height_side = np.arange(0,height*step+step, step, dtype="complex128")
  height_side *= complex(0,-1)

  grid = width_side + height_side.reshape(height+1,1)
  grid += top_left
  return grid

def get_escape_time_color_arr(c_arr: np.ndarray, max_iterations: int) -> np.ndarray:
  """"returns an nd array with float values pertaining to the escape values of c_arr
  input: c_arr which is the complex number grid used to generate mandelbrot image
         max_iterations is the int parameter used for calculating the escape time
  output: ndarray which holds the float values which when converted to gray scale will generate
          a mandelbrot image"""
  whole_grid = np.zeros(c_arr.shape)
  row, col = whole_grid.shape
  for i in range(row):
    for j in range(col):
      escape = get_escape_time(c_arr[i,j], max_iterations)
      if escape is None:
        whole_grid[i,j] = 0
      else:
        whole_grid[i,j] = (max_iterations-escape+1) / (max_iterations+1)

  return whole_grid
