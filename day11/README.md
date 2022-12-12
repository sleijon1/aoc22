# Modulo fun stuff

```python
X%K%n == x%n if K | n

r = x%K

x = K*a + r

x = (b*n*a + r) 

x % n = (b*n*a + r) % n

(b*n*a + r) % n = (b*n*a % n + r % n) % n

r % n % n = r % n = x%K%n
```

[Distributiveness](https://en.wikipedia.org/wiki/Modulo_operation) of modulo operation 



So basically whenever we want to check divisibility of very large numbers we can create a product of the numbers we wish to check divisibility for and just keep track of X%K, X being the large number, K being the product. X%K will essentially hold all information necessary, to check divisibilty for our small numbers such that we only need to deal with the magnitude of K which is determined by the numbers which we want to check for divisibility.


After reading reddit there is also something about mathematical [rings](https://en.wikipedia.org/wiki/Ring_(mathematics)) here which I do not know about and I should look it up.