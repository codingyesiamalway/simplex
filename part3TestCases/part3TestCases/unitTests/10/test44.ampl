var x1 >=0 ;
var x2 >=0 ;
var x3 >=0 ;
var x4 >=0 ;
var x5 >=0 ;
var x6 >=0 ;
var x7 >=0 ;
var x8 >=0 ;
var x9 >=0 ;
var x10 >=0 ;
var x11 >=0 ;
var x12 >=0 ;
var x13 >=0 ;
var x14 >=0 ;
var x15 >=0 ;
var x16 >=0 ;
var x17 >=0 ;
maximize obj: 0.0  + 0.0 * x1   + 2.0 * x2   -5.0 * x3   + 0.0 * x4   -3.0 * x5   -4.0 * x6   -4.0 * x7   + 0.0 * x8   -1.0 * x9 ;
c1: x10 = -2.0  + 7.0 * x1  + 3.0 * x2  + 7.0 * x3  + 8.0 * x4  + 5.0 * x5  + 10.0 * x6  + 8.0 * x7  + 3.0 * x8  + 8.0 * x9 ;
c2: x11 = -3.0  + 1.0 * x1  -10.0 * x2  + 10.0 * x3  + 1.0 * x4  -5.0 * x5  + 7.0 * x6  -7.0 * x7  + 6.0 * x8  + 4.0 * x9 ;
c3: x12 = 1.0  + 0.0 * x1  + 9.0 * x2  -8.0 * x3  -9.0 * x4  + 9.0 * x5  + 1.0 * x6  -6.0 * x7  -4.0 * x8  + 5.0 * x9 ;
c4: x13 = -2.0  -10.0 * x1  -5.0 * x2  -9.0 * x3  + 9.0 * x4  -4.0 * x5  -1.0 * x6  -3.0 * x7  + 2.0 * x8  -1.0 * x9 ;
c5: x14 = 1.0  + 1.0 * x1  -10.0 * x2  + 5.0 * x3  -1.0 * x4  -6.0 * x5  -10.0 * x6  -4.0 * x7  + 6.0 * x8  + 9.0 * x9 ;
c6: x15 = 3.0  + 6.0 * x1  + 3.0 * x2  -10.0 * x3  + 10.0 * x4  + 10.0 * x5  -5.0 * x6  -8.0 * x7  -3.0 * x8  + 5.0 * x9 ;
c7: x16 = 3.0  -8.0 * x1  + 3.0 * x2  -8.0 * x3  -10.0 * x4  -9.0 * x5  + 1.0 * x6  -7.0 * x7  -3.0 * x8  + 5.0 * x9 ;
c8: x17 = 1.0  -4.0 * x1  + 3.0 * x2  + 9.0 * x3  + 8.0 * x4  -8.0 * x5  + 7.0 * x6  -6.0 * x7  + 0.0 * x8  -10.0 * x9 ;
solve; 
display 0.0  + 0.0 * x1   + 2.0 * x2   -5.0 * x3   + 0.0 * x4   -3.0 * x5   -4.0 * x6   -4.0 * x7   + 0.0 * x8   -1.0 * x9 ;
 
 end; 
