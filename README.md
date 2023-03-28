# graphix
Candle Chart Data Visualizer

Goal: Self-made library (graphix.py) for base functions in drawing a candle chart graph, e.g draw_candle draw_grid etc.
      Self-made library (bigraphix.py) for integrating said functions with selenium scraping data from binance to display crypto trading pair data. [SEPARATE REPO]

(graphix.py)
v0.0.1:
  Drawing rectangle based on 4x tuple data (open,close,high,low) displaying green on positive / red on negative
  Drawing high line based on same tuple data provided
  Drawing grid based on window size as well as provided offset size.
  
Both libraries will be updated on an identical basis, so that bigraphix v0.0.1 integrates with graphix v0.0.1 functions etc. Using bigraphix will not necessarily require an identical version of graphix, and vice versa, but differentiating versions could potentially cause issues if more recent versions of bigraphix rely on bug fixes in future versions of graphix that update older functions.
