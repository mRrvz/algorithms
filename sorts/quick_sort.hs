qsort :: Ord a => [a] -> [a]
qsort [] = []
qsort (x:xs) = smaller ++ [x] ++ biggest
    where smaller = qsort [y | y <- xs, y <= x]
          biggest = qsort [y | y <- xs, y > x]


main :: IO ()
main = do
   print $ qsort [1, 7, 23, 31, 311, -1, -2, 5, 7] 
