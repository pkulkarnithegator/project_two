def get_julia(c:complex, max_iterations:int, z:complex) -> int | None:
  """
  Returns the number of iterations before the complex number following the
  Mandelbrot sequence exceeds a magnitude of 2

  Input: c for starting complex number, and max_iterations determining number of steps until to stop
  Output: int value for number of iterations until complex number magnituded is greater than 2 or
            None if magnitude is lower or equal to 2 even after completing max_iterations
  """
  if abs(z) > max(abs(c),2):
    return 0
  for i in range(max_iterations):
    z=z**2 + c
    if abs(z) > max(abs(c),2):
      return i+1
  return None


def get_julia_color_arr(z_arr: np.ndarray, c:complex, max_iterations: int) -> np.ndarray:
  """"returns an nd array with float values pertaining to the escape values of c_arr
  input: c_arr which is the complex number grid used to generate mandelbrot image
         max_iterations is the int parameter used for calculating the escape time
  output: ndarray which holds the float values which when converted to gray scale will generate
          a mandelbrot image"""
  whole_grid = np.zeros(z_arr.shape)
  row, col = whole_grid.shape
  for i in range(row):
    for j in range(col):
      escape = get_julia(c, max_iterations, z_arr[i,j])
      if escape is None:
        whole_grid[i,j] = 0
      else:
        whole_grid[i,j] = (max_iterations-escape+1) / (max_iterations+1)

  return whole_grid
