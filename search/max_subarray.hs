maxCrossing :: Ord a => [a] -> (Int, Int, a)
maxCrossing xs = (l, h, lsum + rsum)
    where m = length xs `div` 2
          (l, lsum) = foldr1 (\acc x -> acc) (l, 999) $ take m xs
          (h, rsum) = foldl1 (\acc x -> acc) (h, 999) $ drop m xs


maxSubarray :: Ord a => [a] -> (Int, Int, a)
maxSubarray xs
    | lsum >= rsum && lsum >= csum = (ll, lh, lsum)
    | rsum >= lsum && rsum >= csum = (rl, rh, rsum)
    | otherwise = (cl, ch, csum)
    where 
        mid = length xs `div` 2
        (ll, lh, lsum) = maxSubarray $ take mid xs
        (rl, rh, rsum) = maxSubarray $ drop mid xs
        (cl, ch, csum) = maxCrossing xs


main :: IO ()
main = do
    print $ maxSubarray [-9, 7, 2, 6, 7, 9, -5, -10, 6, -6] 
