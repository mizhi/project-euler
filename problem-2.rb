#!/usr/bin/env ruby

def fib(n)
  if n == 0 or n == 1
    1
  else
    fib(n-1) + fib(n-2)
  end
end

def fib_nonrec(n)
  fn1 = 1
  fn2 = 0
  fn = fn1 + fn2

  for i in 1..n
    fn  = fn1 + fn2
    fn2 = fn1
    fn1 = fn
  end
  fn
end
