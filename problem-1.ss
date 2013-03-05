
;; sums numbers in nums if the number
;; makes num-pred? true.
(define sum-if
  (lambda (num-pred? nums)
    (cond
      ((null? nums) 0)
      (else 
       (+ 
        (if (num-pred? (car nums))
            (car nums)
            0)
        (sum-if num-pred? (cdr nums)))))))

;; returns a list of positive integers
(define make-pos-num-list 
  (lambda (n)
    (cond 
      ((< n 0) '())
      (else
       (cons n (make-pos-num-list (- n 1)))))))

;; predicate if n is divided by m
(define multiple-of
  (lambda (n m)
    (= 0
       (modulo n m))))

(sum-if 
 (lambda (x) 
   (or 
    (multiple-of x 3) 
    (multiple-of x 5)))
 (make-pos-num-list 999))
