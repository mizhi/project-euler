#!/usr/bin/env ruby

(0...1000).reduce(0) { |accum,x| accum + if x % 3 == 0 or x % 5 == 0; x else 0; end }
