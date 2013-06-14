#!/usr/bin/env ruby -w

#
# Dumb recursive function
#
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

puts((1...1000).reduce(0) { |memo,x|
  fb = fib_nonrec(x)
  if fb % 2 == 0 and fb < 4000000
    memo + fb
  else
    memo
  end
})

#
# Just better to do it like this rather than calling the fib
# functions over and over.
#
sum = 0
fn,fn1,fn2 = 1,1,0
until fn >= 4000000
  fn = fn1 + fn2
  fn2 = fn1
  fn1 = fn

  if fn % 2 == 0
    sum += fn
  end
end

puts sum

#
# Or, let's try a class
#
class FibMem
  def compute(n)
    @values = {0 => 1, 1 => 1} if !defined?(@values)
    if @values.has_key?(n)
      @values[n]
    else
      @values[n] = self.compute(n-1) + self.compute(n-2)
    end
  end
end

mem = FibMem.new
puts((1...1000).reduce(0) { |memo,x|
       fb = mem.compute(x)
       if fb % 2 == 0 and fb < 4000000
         memo + fb
       else
         memo
       end
     })
