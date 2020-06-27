mergeSort :: Ord a => [a] -> [a]
mergeSort (x:[]) = [x]
mergeSort xs = merge (mergeSort left) (mergeSort right) 
    where middle = length xs `div` 2
          left = take middle xs
          right = drop middle xs

merge :: Ord a => [a] -> [a] -> [a]
merge left []    = left
merge [] right   = right
merge left right = 
    if head left < head right 
        then head left : merge (tail left) right
        else head right : merge left (tail right)

main :: IO ()
main = do
    print $ mergeSort [5, 3, 6, 10, -1, 15, 14, -2, 5]
