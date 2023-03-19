import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_case_100(self):
        """Testcase 100 """
        input =	"""a: float;"""
        expect ="""Program([
	VarDecl(a, FloatType)
])""" 
        self.assertTrue(TestAST.test(input, expect, 100))
    def test_case_101(self):
        """Testcase 101 """
        input =	"""a: integer;"""
        expect ="""Program([
	VarDecl(a, IntegerType)
])""" 
        self.assertTrue(TestAST.test(input, expect, 101))
    def test_case_102(self):
        """Testcase 102 """
        input =	"""a: integer = 1;"""
        expect ="""Program([
	VarDecl(a, IntegerType, IntegerLit(1))
])""" 
        self.assertTrue(TestAST.test(input, expect, 102))
    def test_case_103(self):
        """Testcase 103 """
        input =	"""a: integer = 10.0;"""
        expect ="""Program([
	VarDecl(a, IntegerType, FloatLit(10.0))
])""" 
        self.assertTrue(TestAST.test(input, expect, 103))
    def test_case_104(self):
        """Testcase 104 """
        input =	"""a: integer = "str";"""
        expect ="""Program([
	VarDecl(a, IntegerType, StringLit(str))
])""" 
        self.assertTrue(TestAST.test(input, expect, 104))
    def test_case_105(self):
        """Testcase 105 """
        input =	"""a: integer = b;"""
        expect ="""Program([
	VarDecl(a, IntegerType, Id(b))
])""" 
        self.assertTrue(TestAST.test(input, expect, 105))
    def test_case_106(self):
        """Testcase 106 """
        input =	"""a: boolean = foo(1);"""
        expect ="""Program([
	VarDecl(a, BooleanType, FuncCall(foo, [IntegerLit(1)]))
])""" 
        self.assertTrue(TestAST.test(input, expect, 106))
    def test_case_107(self):
        """Testcase 107 """
        input =	"""a: boolean = true;"""
        expect ="""Program([
	VarDecl(a, BooleanType, BooleanLit(True))
])""" 
        self.assertTrue(TestAST.test(input, expect, 107))
    def test_case_108(self):
        """Testcase 108 """
        input =	"""a, b: boolean = 1, 2;"""
        expect ="""Program([
	VarDecl(a, BooleanType, IntegerLit(1))
	VarDecl(b, BooleanType, IntegerLit(2))
])""" 
        self.assertTrue(TestAST.test(input, expect, 108))
    def test_case_109(self):
        """Testcase 109 """
        input =	"""a: boolean = x + 1;"""
        expect ="""Program([
	VarDecl(a, BooleanType, BinExpr(+, Id(x), IntegerLit(1)))
])""" 
        self.assertTrue(TestAST.test(input, expect, 109))
    #----------------------------------------------------------------------------------
     #----------------------------------------------------------------------------------
    def test_case_110(self):
        """Testcase 110 """
        input =	"""a: integer;
                   a, b: boolean = 1, 2;
                   c: string;
        """
        expect ="""Program([
	VarDecl(a, IntegerType)
	VarDecl(a, BooleanType, IntegerLit(1))
	VarDecl(b, BooleanType, IntegerLit(2))
	VarDecl(c, StringType)
])""" 
        self.assertTrue(TestAST.test(input, expect, 110))
    def test_case_111(self):
        """Testcase 111 """
        input =	"""a: integer;
                   
        """
        expect ="""Program([
	VarDecl(a, IntegerType)
])""" 
        self.assertTrue(TestAST.test(input, expect, 111))
    def test_case_112(self):
        """Testcase 112 """
        input =	"""a: integer = 1;
            main: function void(){
                while( a==0 ){
                    x = f(2);
                    if(x==3){
                        break;
                    }
                }
            }
        """
        expect ="""Program([
	VarDecl(a, IntegerType, IntegerLit(1))
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(==, Id(a), IntegerLit(0)), BlockStmt([AssignStmt(Id(x), FuncCall(f, [IntegerLit(2)])), IfStmt(BinExpr(==, Id(x), IntegerLit(3)), BlockStmt([BreakStmt()]))]))]))
])""" 
        self.assertTrue(TestAST.test(input, expect, 112))
    def test_case_113(self):
        """Testcase 113 """
        input =	"""a: integer = 10.0;
            main: function void(){
                if(a>5){
                    x = a +5;
                }
                else {
                    x = a +6;
                }
            }
        """
        expect ="""Program([
	VarDecl(a, IntegerType, FloatLit(10.0))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), IntegerLit(5)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(a), IntegerLit(5)))]), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(a), IntegerLit(6)))]))]))
])""" 
        self.assertTrue(TestAST.test(input, expect, 113))
    def test_case_114(self):
        """Testcase 114 """
        input =	"""a: integer = "str";
            main: function void(){
                   do {
                      a = a+1;
                      x = foo(2,3+4);
                      printf(a);
                   } 
                   while(a==0);
            }
        """
        expect ="""Program([
	VarDecl(a, IntegerType, StringLit(str))
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), IntegerLit(0)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), AssignStmt(Id(x), FuncCall(foo, [IntegerLit(2), BinExpr(+, IntegerLit(3), IntegerLit(4))])), CallStmt(printf, Id(a))]))]))
])""" 
        self.assertTrue(TestAST.test(input, expect, 114))
    def test_case_115(self):
        """Testcase 115 """
        input =	"""a: integer = b;
                   a: function float(x: integer){
                        x = x+1;
                        return x;
                   } 
        """
        expect ="""Program([
	VarDecl(a, IntegerType, Id(b))
	FuncDecl(a, FloatType, [Param(x, IntegerType)], None, BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1))), ReturnStmt(Id(x))]))
])""" 
        self.assertTrue(TestAST.test(input, expect, 115))
    def test_case_116(self):
        """Testcase 116 """
        input =	"""a: boolean = foo(1);
                   a: function integer(){
                        return 5;
                   } 
                    """
        expect ="""Program([
	VarDecl(a, BooleanType, FuncCall(foo, [IntegerLit(1)]))
	FuncDecl(a, IntegerType, [], None, BlockStmt([ReturnStmt(IntegerLit(5))]))
])""" 
        self.assertTrue(TestAST.test(input, expect, 116))
    def test_case_117(self):
        """Testcase 117 """
        input =	"""arr: array [2, 3] of integer;"""
        expect ="""Program([
	VarDecl(arr, ArrayType([2, 3], IntegerType))
])""" 
        self.assertTrue(TestAST.test(input, expect, 117))
    def test_case_118(self):
        """Testcase 118 """
        input =	"""arr: array [2, 3] of float;"""
        expect ="""Program([
	VarDecl(arr, ArrayType([2, 3], FloatType))
])""" 
        self.assertTrue(TestAST.test(input, expect, 118))
    def test_case_119(self):
        """Testcase 119 """
        input =	"""a: boolean = x + 1;
                    func: function integer(){
                        do {
                            a = a+1;
                            x = foo(2,3+4);
                            printf(a);
                            if(a>5){
                                x = a +5;
                            }
                            else {
                                x = a +6;
                            }

                        } 
                        while(a==0);
                    }
        """
        expect ="""Program([
	VarDecl(a, BooleanType, BinExpr(+, Id(x), IntegerLit(1)))
	FuncDecl(func, IntegerType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), IntegerLit(0)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), AssignStmt(Id(x), FuncCall(foo, [IntegerLit(2), BinExpr(+, IntegerLit(3), IntegerLit(4))])), CallStmt(printf, Id(a)), IfStmt(BinExpr(>, Id(a), IntegerLit(5)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(a), IntegerLit(5)))]), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(a), IntegerLit(6)))]))]))]))
])""" 
        self.assertTrue(TestAST.test(input, expect, 119))

        #-----------------------------------------------------------------------------------------
        #----------------------------------------------------------------------------------------
    def test_case_120(self):
        """ Testcase 120 """
        input =	"""a: boolean = x + 1;
                    func: function integer(){
                        do {
                            a = a+1;
                            x = foo(2,3+4);
                            printf(a);
                            if(a>5){
                                x = a +5;
                            }
                            else {
                                x = a +6;
                            }

                        } 
                        while(a==0);
                    }
                    main: function auto(a: integer, arr: array [2, 3] of float){
                        return 1;
                    }
                    """
        expect ="""Program([
	VarDecl(a, BooleanType, BinExpr(+, Id(x), IntegerLit(1)))
	FuncDecl(func, IntegerType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), IntegerLit(0)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), AssignStmt(Id(x), FuncCall(foo, [IntegerLit(2), BinExpr(+, IntegerLit(3), IntegerLit(4))])), CallStmt(printf, Id(a)), IfStmt(BinExpr(>, Id(a), IntegerLit(5)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(a), IntegerLit(5)))]), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(a), IntegerLit(6)))]))]))]))
	FuncDecl(main, AutoType, [Param(a, IntegerType), Param(arr, ArrayType([2, 3], FloatType))], None, BlockStmt([ReturnStmt(IntegerLit(1))]))
])""" 
        self.assertTrue(TestAST.test(input, expect, 120))
    def test_case_121(self):
        """Testcase 121 """
        input =	"""a: boolean = x + 1;
                    func: function integer(){
                        do {
                            a = a+1;
                            x = foo(2,3+4);
                            printf(a);
                            if(a>5){
                                x = a +5;
                            }
                            else {
                                x = a +6;
                            }

                        } 
                        while(a==0);
                    }
                    main: function auto(a: integer, arr: array [2, 3] of float){
                        arr[1+1] = a;
                        return a[2];
                    }
                    """
        expect ="""Program([
	VarDecl(a, BooleanType, BinExpr(+, Id(x), IntegerLit(1)))
	FuncDecl(func, IntegerType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), IntegerLit(0)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), AssignStmt(Id(x), FuncCall(foo, [IntegerLit(2), BinExpr(+, IntegerLit(3), IntegerLit(4))])), CallStmt(printf, Id(a)), IfStmt(BinExpr(>, Id(a), IntegerLit(5)), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(a), IntegerLit(5)))]), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(a), IntegerLit(6)))]))]))]))
	FuncDecl(main, AutoType, [Param(a, IntegerType), Param(arr, ArrayType([2, 3], FloatType))], None, BlockStmt([AssignStmt(ArrayCell(arr, [BinExpr(+, IntegerLit(1), IntegerLit(1))]), Id(a)), ReturnStmt(ArrayCell(a, [IntegerLit(2)]))]))
])""" 
        self.assertTrue(TestAST.test(input, expect, 121))
    def test_case_122(self):
        """Testcase 122 """
        input =	"""a: integer = 1;
                    b: float = 2.5;
                    c: string = "Hello";
                    arr: array [2, 3] of integer ;

                    func: function auto(x: integer, y: integer) {
                        z: integer;
                        z = x + y;
                        return z;
                    }

                    main: function void() {
                        result: integer;
                        result = func(2, 3);
                        if (result > 5) {
                            printf("The result is greater than 5.");
                        } else {
                            printf("The result is less than or equal to 5.");
                        }
                        for(i=0,i<3,i+1){
                            a= a+1;
                        }
                        while (a < 10) {
                            a = a + 1;
                        }

                    }"""
        expect ="""Program([
	VarDecl(a, IntegerType, IntegerLit(1))
	VarDecl(b, FloatType, FloatLit(2.5))
	VarDecl(c, StringType, StringLit(Hello))
	VarDecl(arr, ArrayType([2, 3], IntegerType))
	FuncDecl(func, AutoType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([VarDecl(z, IntegerType), AssignStmt(Id(z), BinExpr(+, Id(x), Id(y))), ReturnStmt(Id(z))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(result, IntegerType), AssignStmt(Id(result), FuncCall(func, [IntegerLit(2), IntegerLit(3)])), IfStmt(BinExpr(>, Id(result), IntegerLit(5)), BlockStmt([CallStmt(printf, StringLit(The result is greater than 5.))]), BlockStmt([CallStmt(printf, StringLit(The result is less than or equal to 5.))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(3)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))])), WhileStmt(BinExpr(<, Id(a), IntegerLit(10)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]))]))
])""" 
        self.assertTrue(TestAST.test(input, expect, 122))
    def test_case_123(self):
        """Testcase 123 """
        input =	"""a: integer = 10.0;
            main: function void(){
                for(i=0,i<3,i+1){
                    a= a+1;
                }
            }
                """
        expect ="""Program([
	VarDecl(a, IntegerType, FloatLit(10.0))
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(3)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]))]))
])""" 
        self.assertTrue(TestAST.test(input, expect, 123))
    def test_case_124(self):
        """Testcase 124 """
        input =	"""aa: integer = 1;
                    b: float = 2.5;
                    c: string = "Hello";
                    arr: array [2, 3] of integer ;

                    func: function auto(x: integer, y: integer) {
                        z: integer;
                        z = x + y;
                        return z;
                    }

                    main: function void() {
                        result: integer;
                        result = func(2, 3);
                        if (result > 5) {
                            printf("The result is greater than 5.");
                        } else {
                            printf("The result is less than or equal to 5.");
                        }
                        for(i=0,i<3,i+1){
                            a= a+1;
                            if(a>5){
                                break;
                            }
                            else{
                                continue;
                            }
                        }
                        while (a < 10) {
                            a = a + 1;
                        }

                    }"""
        expect ="""Program([
	VarDecl(aa, IntegerType, IntegerLit(1))
	VarDecl(b, FloatType, FloatLit(2.5))
	VarDecl(c, StringType, StringLit(Hello))
	VarDecl(arr, ArrayType([2, 3], IntegerType))
	FuncDecl(func, AutoType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([VarDecl(z, IntegerType), AssignStmt(Id(z), BinExpr(+, Id(x), Id(y))), ReturnStmt(Id(z))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(result, IntegerType), AssignStmt(Id(result), FuncCall(func, [IntegerLit(2), IntegerLit(3)])), IfStmt(BinExpr(>, Id(result), IntegerLit(5)), BlockStmt([CallStmt(printf, StringLit(The result is greater than 5.))]), BlockStmt([CallStmt(printf, StringLit(The result is less than or equal to 5.))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(3)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), IfStmt(BinExpr(>, Id(a), IntegerLit(5)), BlockStmt([BreakStmt()]), BlockStmt([ContinueStmt()]))])), WhileStmt(BinExpr(<, Id(a), IntegerLit(10)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]))]))
])""" 
        self.assertTrue(TestAST.test(input, expect, 124))
    def test_case_125(self):
        """Testcase 125 """
        input =	""" aa: integer = 1;
                    b: float = 2.5;
                    c: string = "Hello";
                    arr: array [2, 3] of integer;

                    func: function auto(x: integer, y: integer) {
                        z: integer;
                        z = x + y;
                        return z;
                    }

                    main: function void() {
                        result: integer;
                        result = func(2, 3);
                        if (result > 5) {
                            printf("The result is greater than 5.");
                        } else if (result == 5) {
                            printf("The result is equal to 5.");
                        } else {
                            printf("The result is less than 5.");
                        }
                        for (i = 0, i < 3, i + 1) {
                            a = a + 1;
                            if (a > 5) {
                                break;
                            } else {
                                continue;
                            }
                        }
                        printf("The final value of a is %d.", a);
                        while (a < 10) {
                            a = a + 1;
                            if (a % 2 == 0) {
                                printf("%d is even.", a);
                            } else {
                                printf("%d is odd.", a);
                            }
                            for (j = 0, j < 3,  j + 1) {
                                arr[a % 2, j] = a + j;
                            }
                        }
                        printf("The final value of a is %d.", a);
                        printf("The final value of arr is:");
                        for (i = 0, i < 2, i + 1) {
                            for (j = 0, j < 3,  j + 1) {
                                printf("%d ", arr[i, j]);
                            }
                            printf("\\n");
                        }
                    }"""
        expect ="""Program([
	VarDecl(aa, IntegerType, IntegerLit(1))
	VarDecl(b, FloatType, FloatLit(2.5))
	VarDecl(c, StringType, StringLit(Hello))
	VarDecl(arr, ArrayType([2, 3], IntegerType))
	FuncDecl(func, AutoType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([VarDecl(z, IntegerType), AssignStmt(Id(z), BinExpr(+, Id(x), Id(y))), ReturnStmt(Id(z))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(result, IntegerType), AssignStmt(Id(result), FuncCall(func, [IntegerLit(2), IntegerLit(3)])), IfStmt(BinExpr(>, Id(result), IntegerLit(5)), BlockStmt([CallStmt(printf, StringLit(The result is greater than 5.))]), IfStmt(BinExpr(==, Id(result), IntegerLit(5)), BlockStmt([CallStmt(printf, StringLit(The result is equal to 5.))]), BlockStmt([CallStmt(printf, StringLit(The result is less than 5.))]))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(3)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), IfStmt(BinExpr(>, Id(a), IntegerLit(5)), BlockStmt([BreakStmt()]), BlockStmt([ContinueStmt()]))])), CallStmt(printf, StringLit(The final value of a is %d.), Id(a)), WhileStmt(BinExpr(<, Id(a), IntegerLit(10)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), IfStmt(BinExpr(==, BinExpr(%, Id(a), IntegerLit(2)), IntegerLit(0)), BlockStmt([CallStmt(printf, StringLit(%d is even.), Id(a))]), BlockStmt([CallStmt(printf, StringLit(%d is odd.), Id(a))])), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(3)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(arr, [BinExpr(%, Id(a), IntegerLit(2)), Id(j)]), BinExpr(+, Id(a), Id(j)))]))])), CallStmt(printf, StringLit(The final value of a is %d.), Id(a)), CallStmt(printf, StringLit(The final value of arr is:)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(3)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([CallStmt(printf, StringLit(%d ), ArrayCell(arr, [Id(i), Id(j)]))])), CallStmt(printf, StringLit(\\n))]))]))
])""" 
        self.assertTrue(TestAST.test(input, expect, 125))
    def test_case_126(self):
        """Testcase 126 """
        input =	"""a: boolean = foo(1);
                main: function void() {
                    for (i = 0, i < 5,  i + 1) {
                        for (j = 0, j < 3, j + 1) {
                            arr[i, j] = func(i, j);
                        }
                    }
                    for (i = 0, i < 2,  i + 1) {
                        for (j = 0, j < 3,  j + 1) {
                            printf("%d ", arr[i, j]);
                        }
                        printf("\\n");
                    }
                    a: integer = 1;
                    while (a < 10) {
                        a = a + 1;
                        if (a % 2 == 0) {
                            continue;
                        }
                        printf("%d\\n", a);
                        for (i = 0, i < a, i + 1) {
                            if (i % 2 == 0) {
                                arr[0, i] = func(a, i);
                            } else {
                                arr[1, i] = func(a, i);
                            }
                        }
                        for (i = 0, i < 2, i + 1) {
                            for (j = 0, j < a,  j + 1) {
                                printf("%d ", arr[i, j]);
                            }
                            printf("\\n");
                        }
                        printf("\\n");
                    }
                }"""
        expect ="""Program([
	VarDecl(a, BooleanType, FuncCall(foo, [IntegerLit(1)]))
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(3)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(arr, [Id(i), Id(j)]), FuncCall(func, [Id(i), Id(j)]))]))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(3)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([CallStmt(printf, StringLit(%d ), ArrayCell(arr, [Id(i), Id(j)]))])), CallStmt(printf, StringLit(\\n))])), VarDecl(a, IntegerType, IntegerLit(1)), WhileStmt(BinExpr(<, Id(a), IntegerLit(10)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), IfStmt(BinExpr(==, BinExpr(%, Id(a), IntegerLit(2)), IntegerLit(0)), BlockStmt([ContinueStmt()])), CallStmt(printf, StringLit(%d\\n), Id(a)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(a)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), BlockStmt([AssignStmt(ArrayCell(arr, [IntegerLit(0), Id(i)]), FuncCall(func, [Id(a), Id(i)]))]), BlockStmt([AssignStmt(ArrayCell(arr, [IntegerLit(1), Id(i)]), FuncCall(func, [Id(a), Id(i)]))]))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(a)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([CallStmt(printf, StringLit(%d ), ArrayCell(arr, [Id(i), Id(j)]))])), CallStmt(printf, StringLit(\\n))])), CallStmt(printf, StringLit(\\n))]))]))
])""" 
        self.assertTrue(TestAST.test(input, expect, 126))
    def test_case_127(self):
        """Testcase 127 """
        input =	"""a: boolean = true;
        sum: function auto(x: integer, y: integer) {
            return x + y;
        }

        prod: function auto(x: float, y: float) {
            return x * y;
        }

        main: function void() {
            i: integer = 0;
            j: integer = 0;

            // Use a while loop to find the first value of i such that i^2 >= 100.
            while (i * i < 100) {
                i = i + 1;
            }
            printf("The smallest integer whose square is greater than or equal to 100 is %d\\n", i);

            // Use a do-while loop to print out the values of j from 10 to 1.
            j = 10;
            do {
                printf("%d\\n", j);
                j = j - 1;
            } while (j > 0);

            // Use a for loop to calculate the sum of the numbers from 1 to 10.
            total: integer = 0;
            for (i = 1, i <= 10, i + 1) {
                total = sum(total, i);
            }
            printf("The sum of the numbers from 1 to 10 is %d\\n", total);

            // Use an if statement to determine if b is greater than 3.0.
            if (b > 3.0) {
                printf("b is greater than 3.0\\n");
            } else {
                printf("b is less than or equal to 3.0\\n");
            }

            // Use a nested for loop to calculate the product of the elements of d.
            product: float = 1.0;
            for (i = 0, i < 2,  i + 1) {
                for (j = 0, j < 3,  j + 1) {
                    product = prod(product, d[i]);
                }
            }
            printf("The product of the elements of d is %.2f\\n", product);

            // Use a function call to calculate the sum of a and the result of the sum function.
            result: integer = sum(a, sum(3, 4));
            printf("The sum of a, 3, and 4 is %d\\n", result);
        }"""
        expect ="""Program([
	VarDecl(a, BooleanType, BooleanLit(True))
	FuncDecl(sum, AutoType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(x), Id(y)))]))
	FuncDecl(prod, AutoType, [Param(x, FloatType), Param(y, FloatType)], None, BlockStmt([ReturnStmt(BinExpr(*, Id(x), Id(y)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), VarDecl(j, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(<, BinExpr(*, Id(i), Id(i)), IntegerLit(100)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), CallStmt(printf, StringLit(The smallest integer whose square is greater than or equal to 100 is %d\\n), Id(i)), AssignStmt(Id(j), IntegerLit(10)), DoWhileStmt(BinExpr(>, Id(j), IntegerLit(0)), BlockStmt([CallStmt(printf, StringLit(%d\\n), Id(j)), AssignStmt(Id(j), BinExpr(-, Id(j), IntegerLit(1)))])), VarDecl(total, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(total), FuncCall(sum, [Id(total), Id(i)]))])), CallStmt(printf, StringLit(The sum of the numbers from 1 to 10 is %d\\n), Id(total)), IfStmt(BinExpr(>, Id(b), FloatLit(3.0)), BlockStmt([CallStmt(printf, StringLit(b is greater than 3.0\\n))]), BlockStmt([CallStmt(printf, StringLit(b is less than or equal to 3.0\\n))])), VarDecl(product, FloatType, FloatLit(1.0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(3)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(Id(product), FuncCall(prod, [Id(product), ArrayCell(d, [Id(i)])]))]))])), CallStmt(printf, StringLit(The product of the elements of d is %.2f\\n), Id(product)), VarDecl(result, IntegerType, FuncCall(sum, [Id(a), FuncCall(sum, [IntegerLit(3), IntegerLit(4)])])), CallStmt(printf, StringLit(The sum of a, 3, and 4 is %d\\n), Id(result))]))
])""" 
        self.assertTrue(TestAST.test(input, expect, 127))
    def test_case_128(self):
        """Testcase 128 """
        input =	"""sum: function auto(x: integer, y: integer) {
            return x + y;
        }

        prod: function auto(x: float, y: float) {
            return x * y;
        }

        main: function void() {
            i: integer = 0;
            j: integer = 0;

            // Use a while loop to calculate the factorial of 5.
            factorial: integer = 1;
            while (i < 5) {
                i = i + 1;
                factorial = factorial * i;
            }
            printf("The factorial of 5 is %d\\n", factorial);

            // Use a do-while loop to read a number from the user and determine if it is positive.
            num: integer;
            do {
                printf("Enter a positive number: ");
                scanf("%d", num);
            } while (num <= 0);
            printf("You entered %d, which is positive.\\n", num);

            // Use a for loop to calculate the sum of the odd numbers from 1 to 100.
            odd_sum: integer = 0;
            for (i = 1, i <= 100,  i + 2) {
                odd_sum = sum(odd_sum, i);
            }
            printf("The sum of the odd numbers from 1 to 100 is %d\\n", odd_sum);

            // Use an if statement to determine if b is greater than or equal to 2.0 and less than or equal to 3.0.
            if ((b >= 2.0) &&( b <= 3.0)) {
                printf("b is between 2.0 and 3.0, inclusive.\\n");
            } else {
                printf("b is not between 2.0 and 3.0, inclusive.\\n");
            }

            // Use a nested for loop to calculate the product of the even elements of d.
            even_product: float = 1.0;
            for (i = 0, i < 2, i + 1) {
                for (j = 0, j < 3,  j + 1) {
                    if (d[i] % 2 == 0) {
                        even_product = prod(even_product, d[i]);
                    }
                }
            }
            printf("The product of the even elements of d is %.2f\\n", even_product);

            // Use a function call to calculate the sum of a and the result of the prod function.
            result: float = sum(a, prod(2.0, 3.5));
            printf("The sum of a and the product of 2.0 and 3.5 is %.2f\\n", result);
        }"""
        expect ="""Program([
	FuncDecl(sum, AutoType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(x), Id(y)))]))
	FuncDecl(prod, AutoType, [Param(x, FloatType), Param(y, FloatType)], None, BlockStmt([ReturnStmt(BinExpr(*, Id(x), Id(y)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), VarDecl(j, IntegerType, IntegerLit(0)), VarDecl(factorial, IntegerType, IntegerLit(1)), WhileStmt(BinExpr(<, Id(i), IntegerLit(5)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), AssignStmt(Id(factorial), BinExpr(*, Id(factorial), Id(i)))])), CallStmt(printf, StringLit(The factorial of 5 is %d\\n), Id(factorial)), VarDecl(num, IntegerType), DoWhileStmt(BinExpr(<=, Id(num), IntegerLit(0)), BlockStmt([CallStmt(printf, StringLit(Enter a positive number: )), CallStmt(scanf, StringLit(%d), Id(num))])), CallStmt(printf, StringLit(You entered %d, which is positive.\\n), Id(num)), VarDecl(odd_sum, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(2)), BlockStmt([AssignStmt(Id(odd_sum), FuncCall(sum, [Id(odd_sum), Id(i)]))])), CallStmt(printf, StringLit(The sum of the odd numbers from 1 to 100 is %d\\n), Id(odd_sum)), IfStmt(BinExpr(&&, BinExpr(>=, Id(b), FloatLit(2.0)), BinExpr(<=, Id(b), FloatLit(3.0))), BlockStmt([CallStmt(printf, StringLit(b is between 2.0 and 3.0, inclusive.\\n))]), BlockStmt([CallStmt(printf, StringLit(b is not between 2.0 and 3.0, inclusive.\\n))])), VarDecl(even_product, FloatType, FloatLit(1.0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(3)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, ArrayCell(d, [Id(i)]), IntegerLit(2)), IntegerLit(0)), BlockStmt([AssignStmt(Id(even_product), FuncCall(prod, [Id(even_product), ArrayCell(d, [Id(i)])]))]))]))])), CallStmt(printf, StringLit(The product of the even elements of d is %.2f\\n), Id(even_product)), VarDecl(result, FloatType, FuncCall(sum, [Id(a), FuncCall(prod, [FloatLit(2.0), FloatLit(3.5)])])), CallStmt(printf, StringLit(The sum of a and the product of 2.0 and 3.5 is %.2f\\n), Id(result))]))
])""" 
        self.assertTrue(TestAST.test(input, expect, 128))
    def test_case_129(self):
        """Testcase 129 """
        input =	"""a: integer = 1;
                    b: integer = 2;

                    // Define a function to compute the greatest common divisor (GCD) of two integers.
                    gcd: function auto(x: integer, y: integer) {
                        while (y != 0) {
                            r: integer = x % y;
                            x = y;
                            y = r;
                        }
                        return x;
                    }

                    main: function void() {
                        // Calculate the GCD of a and b using the gcd function.
                        g: integer = gcd(a, b);
                        printf("The GCD of %d and %d is %d.\\n", a, b, g);

                        // Use a for loop to calculate the sum of the first 100 integers.
                        s: integer = 0;
                        for (i = 1, i <= 100, i + 1) {
                            s = s + i;
                        }
                        printf("The sum of the first 100 integers is %d.\\n", s);

                        // Use assignments and function calls to compute the value of the expression (a + b) * (a - b) / (a * b).
                        p: integer = a + b;
                        q: integer = a - b;
                        r: integer = a * b;
                        result: float = (p * q) / r;
                        printf("The value of (a + b) * (a - b) / (a * b) is %.2f.\\n", result);
                    }"""
        expect ="""Program([
	VarDecl(a, IntegerType, IntegerLit(1))
	VarDecl(b, IntegerType, IntegerLit(2))
	FuncDecl(gcd, AutoType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(!=, Id(y), IntegerLit(0)), BlockStmt([VarDecl(r, IntegerType, BinExpr(%, Id(x), Id(y))), AssignStmt(Id(x), Id(y)), AssignStmt(Id(y), Id(r))])), ReturnStmt(Id(x))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(g, IntegerType, FuncCall(gcd, [Id(a), Id(b)])), CallStmt(printf, StringLit(The GCD of %d and %d is %d.\\n), Id(a), Id(b), Id(g)), VarDecl(s, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(s), BinExpr(+, Id(s), Id(i)))])), CallStmt(printf, StringLit(The sum of the first 100 integers is %d.\\n), Id(s)), VarDecl(p, IntegerType, BinExpr(+, Id(a), Id(b))), VarDecl(q, IntegerType, BinExpr(-, Id(a), Id(b))), VarDecl(r, IntegerType, BinExpr(*, Id(a), Id(b))), VarDecl(result, FloatType, BinExpr(/, BinExpr(*, Id(p), Id(q)), Id(r))), CallStmt(printf, StringLit(The value of (a + b) * (a - b) / (a * b) is %.2f.\\n), Id(result))]))
])""" 
        self.assertTrue(TestAST.test(input, expect, 129))
    #----------------------------------------------------------------------------------
     #----------------------------------------------------------------------------------
    def test_case_130(self):
        """Testcase 130 """
        input =	"""// Declare and initialize variables.
                    n: integer = 100;
                    sum: integer = 0;
                    prod: integer = 1;
                    count: integer = 0;

                    // Define a function to check if a number is prime.
                    is_prime: function auto(x: integer) {
                        if (x < 2) {
                            return false;
                        } else {
                            for (i = 2, i <= x / 2,  i + 1) {
                                if (x % i == 0) {
                                    return false;
                                }
                            }
                            return true;
                        }
                    }

                    // Define a function to compute the factorial of a number.
                    factorial: function auto(x: integer) {
                        if (x == 0) {
                            return 1;
                        } else {
                            return x * factorial(x - 1);
                        }
                    }

                    main: function void() {
                        // Use a while loop to calculate the sum of the first n odd integers.
                        i: integer = 1;
                        while (i <= n) {
                            sum = sum + i;
                            i = i + 2;
                        }
                        printf("The sum of the first %d odd integers is %d.\\n", n, sum);

                        // Use a for loop to calculate the product of the first n even integers that are not divisible by 3.
                        for (i = 2, count < n, i + 2) {
                            if (i % 3 != 0) {
                                prod = prod * i;
                                count = count + 1;
                            }
                        }
                        printf("The product of the first %d even integers not divisible by 3 is %d.\\n", n, prod);

                        // Use assignments and function calls to compute the value of the expression (n choose 2) * factorial(n - 2) / 2^n.
                        p: integer = factorial(n) / (factorial(2) * factorial(n - 2));
                        q: integer = 2 * n;
                        result: float = p * factorial(n - 2) / q;
                        printf("The value of (n choose 2) * factorial(n - 2) / 2^n is %.2f.\\n", result);

                        // Check if the number n is prime using the is_prime function.
                        if (is_prime(n)) {
                            printf("%d is prime.\\n", n);
                        } else {
                            printf("%d is not prime.\\n", n);
                        }
                    }

        """
        expect ="""Program([
	VarDecl(n, IntegerType, IntegerLit(100))
	VarDecl(sum, IntegerType, IntegerLit(0))
	VarDecl(prod, IntegerType, IntegerLit(1))
	VarDecl(count, IntegerType, IntegerLit(0))
	FuncDecl(is_prime, AutoType, [Param(x, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(x), IntegerLit(2)), BlockStmt([ReturnStmt(BooleanLit(False))]), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, Id(i), BinExpr(/, Id(x), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(x), Id(i)), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(False))]))])), ReturnStmt(BooleanLit(True))]))]))
	FuncDecl(factorial, AutoType, [Param(x, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(0)), BlockStmt([ReturnStmt(IntegerLit(1))]), BlockStmt([ReturnStmt(BinExpr(*, Id(x), FuncCall(factorial, [BinExpr(-, Id(x), IntegerLit(1))])))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(1)), WhileStmt(BinExpr(<=, Id(i), Id(n)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), Id(i))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(2)))])), CallStmt(printf, StringLit(The sum of the first %d odd integers is %d.\\n), Id(n), Id(sum)), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<, Id(count), Id(n)), BinExpr(+, Id(i), IntegerLit(2)), BlockStmt([IfStmt(BinExpr(!=, BinExpr(%, Id(i), IntegerLit(3)), IntegerLit(0)), BlockStmt([AssignStmt(Id(prod), BinExpr(*, Id(prod), Id(i))), AssignStmt(Id(count), BinExpr(+, Id(count), IntegerLit(1)))]))])), CallStmt(printf, StringLit(The product of the first %d even integers not divisible by 3 is %d.\\n), Id(n), Id(prod)), VarDecl(p, IntegerType, BinExpr(/, FuncCall(factorial, [Id(n)]), BinExpr(*, FuncCall(factorial, [IntegerLit(2)]), FuncCall(factorial, [BinExpr(-, Id(n), IntegerLit(2))])))), VarDecl(q, IntegerType, BinExpr(*, IntegerLit(2), Id(n))), VarDecl(result, FloatType, BinExpr(/, BinExpr(*, Id(p), FuncCall(factorial, [BinExpr(-, Id(n), IntegerLit(2))])), Id(q))), CallStmt(printf, StringLit(The value of (n choose 2) * factorial(n - 2) / 2^n is %.2f.\\n), Id(result)), IfStmt(FuncCall(is_prime, [Id(n)]), BlockStmt([CallStmt(printf, StringLit(%d is prime.\\n), Id(n))]), BlockStmt([CallStmt(printf, StringLit(%d is not prime.\\n), Id(n))]))]))
])""" 
        self.assertTrue(TestAST.test(input, expect, 130))
    def test_case_131(self):
        """Testcase 131 """
        input =	"""n: integer = 10;
                    a: float = 1.0;
                    b: float = 1.0;
                    sum: float = 0.0;
                main: function void(){
                    // Use a while loop to calculate the sum of the first n terms of the Fibonacci sequence.
                    i: integer = 1;
                    while (i <= n) {
                        if (i == 1) {
                            sum = a;
                        } else if (i == 2) {
                            sum = b;
                        } else {
                            sum = a + b;
                            a = b;
                            b = sum;
                        }
                        i = i + 1;
                    }
                    printf("The sum of the first %d terms of the Fibonacci sequence is %.2f.\\n", n, sum);

                    // Use a for loop to calculate the product of the first n positive integers.
                    prod: integer = 1;
                    for (i = 1, i <= n,  i + 1) {
                        prod = prod * i;
                    }
                    printf("The product of the first %d positive integers is %d.\\n", n, prod);

                    // Use an if statement to check if the number n is prime.
                    is_prime: boolean = true;
                    if (n < 2) {
                        is_prime = false;
                    } else {
                        for (i = 2,i <= n / 2, i + 1) {
                            if (n % i == 0) {
                                is_prime = false;
                                break;
                            }
                        }
                    }
                    if (is_prime) {
                        printf("%d is prime.\\n", n);
                    } else {
                        printf("%d is not prime.\\n", n);
                    }
                    }
                   
        """
        expect ="""Program([
	VarDecl(n, IntegerType, IntegerLit(10))
	VarDecl(a, FloatType, FloatLit(1.0))
	VarDecl(b, FloatType, FloatLit(1.0))
	VarDecl(sum, FloatType, FloatLit(0.0))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(1)), WhileStmt(BinExpr(<=, Id(i), Id(n)), BlockStmt([IfStmt(BinExpr(==, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), Id(a))]), IfStmt(BinExpr(==, Id(i), IntegerLit(2)), BlockStmt([AssignStmt(Id(sum), Id(b))]), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(a), Id(b))), AssignStmt(Id(a), Id(b)), AssignStmt(Id(b), Id(sum))]))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), CallStmt(printf, StringLit(The sum of the first %d terms of the Fibonacci sequence is %.2f.\\n), Id(n), Id(sum)), VarDecl(prod, IntegerType, IntegerLit(1)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(prod), BinExpr(*, Id(prod), Id(i)))])), CallStmt(printf, StringLit(The product of the first %d positive integers is %d.\\n), Id(n), Id(prod)), VarDecl(is_prime, BooleanType, BooleanLit(True)), IfStmt(BinExpr(<, Id(n), IntegerLit(2)), BlockStmt([AssignStmt(Id(is_prime), BooleanLit(False))]), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, Id(i), BinExpr(/, Id(n), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), BlockStmt([AssignStmt(Id(is_prime), BooleanLit(False)), BreakStmt()]))]))])), IfStmt(Id(is_prime), BlockStmt([CallStmt(printf, StringLit(%d is prime.\\n), Id(n))]), BlockStmt([CallStmt(printf, StringLit(%d is not prime.\\n), Id(n))]))]))
])""" 
        self.assertTrue(TestAST.test(input, expect, 131))
    def test_case_132(self):
        """Testcase 132 """
        input =	"""// Define a function to calculate the factorial of a number.
                factorial: function auto(n: integer) {
                    if (n < 0) {
                        return -1;
                    } else if (n == 0) {
                        return 1;
                    } else {
                        fact: integer = 1;
                        i: integer = 1;
                        while (i <= n) {
                            fact = fact * i;
                            i = i + 1;
                        }
                        return fact;
                    }
                }

                // Declare and initialize variables.
                x: integer = 5;
                y: float = 2.0;
                result: float = 0.0;
                main: function void(){
                    // Calculate the result using a while loop and the factorial function.
                    i: integer = 0;
                    while (i <= x) {
                        if (i % 2 == 0) {
                            result = result + (y / factorial(i));
                        } else {
                            result = result - (y / factorial(i));
                        }
                        i = i + 1;
                    }
                

                // Output the result.
                printf("The result of the series is %.2f.\\n", result);
                }
        """
        expect ="""Program([
	FuncDecl(factorial, AutoType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(UnExpr(-, IntegerLit(1)))]), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(IntegerLit(1))]), BlockStmt([VarDecl(fact, IntegerType, IntegerLit(1)), VarDecl(i, IntegerType, IntegerLit(1)), WhileStmt(BinExpr(<=, Id(i), Id(n)), BlockStmt([AssignStmt(Id(fact), BinExpr(*, Id(fact), Id(i))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), ReturnStmt(Id(fact))])))]))
	VarDecl(x, IntegerType, IntegerLit(5))
	VarDecl(y, FloatType, FloatLit(2.0))
	VarDecl(result, FloatType, FloatLit(0.0))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(<=, Id(i), Id(x)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), BinExpr(/, Id(y), FuncCall(factorial, [Id(i)]))))]), BlockStmt([AssignStmt(Id(result), BinExpr(-, Id(result), BinExpr(/, Id(y), FuncCall(factorial, [Id(i)]))))])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), CallStmt(printf, StringLit(The result of the series is %.2f.\\n), Id(result))]))
])""" 
        self.assertTrue(TestAST.test(input, expect, 132))
    def test_case_133(self):
        """Testcase 133 """
        input =	"""// Define a function to calculate the nth Fibonacci number.
                    fibonacci: function auto(n: integer) {
                        if (n < 0) {
                            return -1;
                        } else if ((n == 0 )|| (n == 1)) {
                            return n;
                        } else {
                            return fibonacci(n-1) + fibonacci(n-2);
                        }
                    }

                    // Define a function to find the largest number in an array.
                    find_largest: function auto(arr: array [10] of integer) {
                        largest: integer = arr[0];
                        for (i = 1, i < 10, i+ 1) {
                            if (arr[i] > largest) {
                                largest = arr[i];
                            }
                        }
                        return largest;
                    }

                    // Define a function to find the sum of the elements in a row of a matrix.
                    row_sum: function auto(matrix: array [3, 3] of integer, row: integer) {
                        sum: integer = 0;
                        for (i = 0,i < 3, i + 1) {
                            sum = sum + matrix[row, i];
                        }
                        return sum;
                    }
                    main: function void(){
                        // Declare and initialize variables.
                        fib_nums: array [10] of integer;
                        for (i = 0, i < 10, i + 1) {
                            fib_nums[i] = fibonacci(i);
                        }

                        matrix: array [3, 3] of integer;

                        // Find the largest Fibonacci number.
                        largest_fib: integer = find_largest(fib_nums);

                        // Find the row with the largest sum in the matrix.
                        largest_sum: integer = 0;
                        largest_sum_row: integer = -1;
                        for (i = 0, i < 3,i + 1) {
                            sum = row_sum(matrix, i);
                            if (sum > largest_sum) {
                                largest_sum = sum;
                                largest_sum_row = i;
                            }
                        }

                    // Output the results.
                    printf("The largest Fibonacci number is %d.\\n", largest_fib);
                    printf("The row with the largest sum in the matrix is row %d, with a sum of %d.\\n", largest_sum_row, largest_sum);
                    }
                            """
        expect ="""Program([
	FuncDecl(fibonacci, AutoType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(UnExpr(-, IntegerLit(1)))]), IfStmt(BinExpr(||, BinExpr(==, Id(n), IntegerLit(0)), BinExpr(==, Id(n), IntegerLit(1))), BlockStmt([ReturnStmt(Id(n))]), BlockStmt([ReturnStmt(BinExpr(+, FuncCall(fibonacci, [BinExpr(-, Id(n), IntegerLit(1))]), FuncCall(fibonacci, [BinExpr(-, Id(n), IntegerLit(2))])))])))]))
	FuncDecl(find_largest, AutoType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([VarDecl(largest, IntegerType, ArrayCell(arr, [IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(arr, [Id(i)]), Id(largest)), BlockStmt([AssignStmt(Id(largest), ArrayCell(arr, [Id(i)]))]))])), ReturnStmt(Id(largest))]))
	FuncDecl(row_sum, AutoType, [Param(matrix, ArrayType([3, 3], IntegerType)), Param(row, IntegerType)], None, BlockStmt([VarDecl(sum, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(3)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(matrix, [Id(row), Id(i)])))])), ReturnStmt(Id(sum))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(fib_nums, ArrayType([10], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(fib_nums, [Id(i)]), FuncCall(fibonacci, [Id(i)]))])), VarDecl(matrix, ArrayType([3, 3], IntegerType)), VarDecl(largest_fib, IntegerType, FuncCall(find_largest, [Id(fib_nums)])), VarDecl(largest_sum, IntegerType, IntegerLit(0)), VarDecl(largest_sum_row, IntegerType, UnExpr(-, IntegerLit(1))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(3)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), FuncCall(row_sum, [Id(matrix), Id(i)])), IfStmt(BinExpr(>, Id(sum), Id(largest_sum)), BlockStmt([AssignStmt(Id(largest_sum), Id(sum)), AssignStmt(Id(largest_sum_row), Id(i))]))])), CallStmt(printf, StringLit(The largest Fibonacci number is %d.\\n), Id(largest_fib)), CallStmt(printf, StringLit(The row with the largest sum in the matrix is row %d, with a sum of %d.\\n), Id(largest_sum_row), Id(largest_sum))]))
])""" 
        self.assertTrue(TestAST.test(input, expect, 133))
    def test_case_134(self):
        """Testcase 134 """
        input =	"""a: float = 1.0;
                b: float = -5.0;
                c: float = 6.0;
                delta: float = b * b - 4 * a * c;
                x1: float;
                x2: float;
                main: function void(){
                    if (delta > 0) {
                        x1 = (-b + sqrt(delta)) / (2 * a);
                        x2 = (-b - sqrt(delta)) / (2 * a);
                        printf("The equation has two real roots: %.2f and %.2f\\n", x1, x2);
                    } else if (delta == 0) {
                        x1 = -b / (2 * a);
                        printf("The equation has one real root: %.2f\\n", x1);
                    } else {
                        real_part: float = -b / (2 * a);
                        imaginary_part: float = sqrt(-delta) / (2 * a);
                        printf("The equation has two complex roots: %.2f + %.2fi and %.2f - %.2fi\\n", real_part, imaginary_part, real_part, imaginary_part);
                    }
                }
        """
        expect ="""Program([
	VarDecl(a, FloatType, FloatLit(1.0))
	VarDecl(b, FloatType, UnExpr(-, FloatLit(5.0)))
	VarDecl(c, FloatType, FloatLit(6.0))
	VarDecl(delta, FloatType, BinExpr(-, BinExpr(*, Id(b), Id(b)), BinExpr(*, BinExpr(*, IntegerLit(4), Id(a)), Id(c))))
	VarDecl(x1, FloatType)
	VarDecl(x2, FloatType)
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(delta), IntegerLit(0)), BlockStmt([AssignStmt(Id(x1), BinExpr(/, BinExpr(+, UnExpr(-, Id(b)), FuncCall(sqrt, [Id(delta)])), BinExpr(*, IntegerLit(2), Id(a)))), AssignStmt(Id(x2), BinExpr(/, BinExpr(-, UnExpr(-, Id(b)), FuncCall(sqrt, [Id(delta)])), BinExpr(*, IntegerLit(2), Id(a)))), CallStmt(printf, StringLit(The equation has two real roots: %.2f and %.2f\\n), Id(x1), Id(x2))]), IfStmt(BinExpr(==, Id(delta), IntegerLit(0)), BlockStmt([AssignStmt(Id(x1), BinExpr(/, UnExpr(-, Id(b)), BinExpr(*, IntegerLit(2), Id(a)))), CallStmt(printf, StringLit(The equation has one real root: %.2f\\n), Id(x1))]), BlockStmt([VarDecl(real_part, FloatType, BinExpr(/, UnExpr(-, Id(b)), BinExpr(*, IntegerLit(2), Id(a)))), VarDecl(imaginary_part, FloatType, BinExpr(/, FuncCall(sqrt, [UnExpr(-, Id(delta))]), BinExpr(*, IntegerLit(2), Id(a)))), CallStmt(printf, StringLit(The equation has two complex roots: %.2f + %.2fi and %.2f - %.2fi\\n), Id(real_part), Id(imaginary_part), Id(real_part), Id(imaginary_part))])))]))
])""" 
        self.assertTrue(TestAST.test(input, expect, 134))
    def test_case_135(self):
        """Testcase 135 """
        input =	"""// Function to calculate the factorial of a positive integer
                     factorial: function integer(n: integer) {
                        if ((n == 0 )|| (n == 1)) {
                            return 1;
                        } else {
                            return n * factorial(n - 1);
                        }
                    }

                    // Function to calculate the nth Fibonacci number
                    fibonacci: function integer(n: integer) {
                        if ((n == 0) || (n == 1)) {
                            return n;
                        } else {
                            return fibonacci(n - 1) + fibonacci(n - 2);
                        }
                    }

                    // Function to calculate the sum of a geometric series
                     geometric_sum: function integer(a: float, r: float, n: integer) {
                        if (r == 1) {
                            return a * n;
                        } else {
                            return a * (1 - pow(r, n)) / (1 - r);
                        }
                    }

                    // Function to calculate the roots of a quadratic equation
                    quadratic_roots : function integer(a: float, b: float, c: float) {
                        delta: float = b * b - 4 * a * c;
                        x1: float;
                        x2: float;

                        if (delta > 0) {
                            x1 = (-b + sqrt(delta)) / (2 * a);
                            x2 = (-b - sqrt(delta)) / (2 * a);
                            printf("The equation has two real roots: %.2f and %.2f\\n", x1, x2);
                        } else if (delta == 0) {
                            x1 = -b / (2 * a);
                            printf("The equation has one real root: %.2f\\n", x1);
                        } else {
                            real_part: float = -b / (2 * a);
                            imaginary_part: float = sqrt(-delta) / (2 * a);
                            printf("The equation has two complex roots: %.2f + %.2fi and %.2f - %.2fi\\n", real_part, imaginary_part, real_part, imaginary_part);
                        }
                    }

                    // Main function
                    main: function void() {
                        // Calculate the factorial of 5
                        printf("The factorial of 5 is: %d\\n", factorial(5));

                        // Calculate the 10th Fibonacci number
                        printf("The 10th Fibonacci number is: %d\\n", fibonacci(10));

                        // Calculate the sum of the first 5 terms of the geometric series with a = 1 and r = 2
                        printf("The sum of the first 5 terms of the geometric series with a = 1 and r = 2 is: %.2f\\n", geometric_sum(1, 2, 5));

                        // Find the roots of the quadratic equation x^2 - 5x + 6 = 0
                        quadratic_roots(1, -5, 6);
                    }
        """
        expect ="""Program([
	FuncDecl(factorial, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(==, Id(n), IntegerLit(0)), BinExpr(==, Id(n), IntegerLit(1))), BlockStmt([ReturnStmt(IntegerLit(1))]), BlockStmt([ReturnStmt(BinExpr(*, Id(n), FuncCall(factorial, [BinExpr(-, Id(n), IntegerLit(1))])))]))]))
	FuncDecl(fibonacci, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(==, Id(n), IntegerLit(0)), BinExpr(==, Id(n), IntegerLit(1))), BlockStmt([ReturnStmt(Id(n))]), BlockStmt([ReturnStmt(BinExpr(+, FuncCall(fibonacci, [BinExpr(-, Id(n), IntegerLit(1))]), FuncCall(fibonacci, [BinExpr(-, Id(n), IntegerLit(2))])))]))]))
	FuncDecl(geometric_sum, IntegerType, [Param(a, FloatType), Param(r, FloatType), Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(r), IntegerLit(1)), BlockStmt([ReturnStmt(BinExpr(*, Id(a), Id(n)))]), BlockStmt([ReturnStmt(BinExpr(/, BinExpr(*, Id(a), BinExpr(-, IntegerLit(1), FuncCall(pow, [Id(r), Id(n)]))), BinExpr(-, IntegerLit(1), Id(r))))]))]))
	FuncDecl(quadratic_roots, IntegerType, [Param(a, FloatType), Param(b, FloatType), Param(c, FloatType)], None, BlockStmt([VarDecl(delta, FloatType, BinExpr(-, BinExpr(*, Id(b), Id(b)), BinExpr(*, BinExpr(*, IntegerLit(4), Id(a)), Id(c)))), VarDecl(x1, FloatType), VarDecl(x2, FloatType), IfStmt(BinExpr(>, Id(delta), IntegerLit(0)), BlockStmt([AssignStmt(Id(x1), BinExpr(/, BinExpr(+, UnExpr(-, Id(b)), FuncCall(sqrt, [Id(delta)])), BinExpr(*, IntegerLit(2), Id(a)))), AssignStmt(Id(x2), BinExpr(/, BinExpr(-, UnExpr(-, Id(b)), FuncCall(sqrt, [Id(delta)])), BinExpr(*, IntegerLit(2), Id(a)))), CallStmt(printf, StringLit(The equation has two real roots: %.2f and %.2f\\n), Id(x1), Id(x2))]), IfStmt(BinExpr(==, Id(delta), IntegerLit(0)), BlockStmt([AssignStmt(Id(x1), BinExpr(/, UnExpr(-, Id(b)), BinExpr(*, IntegerLit(2), Id(a)))), CallStmt(printf, StringLit(The equation has one real root: %.2f\\n), Id(x1))]), BlockStmt([VarDecl(real_part, FloatType, BinExpr(/, UnExpr(-, Id(b)), BinExpr(*, IntegerLit(2), Id(a)))), VarDecl(imaginary_part, FloatType, BinExpr(/, FuncCall(sqrt, [UnExpr(-, Id(delta))]), BinExpr(*, IntegerLit(2), Id(a)))), CallStmt(printf, StringLit(The equation has two complex roots: %.2f + %.2fi and %.2f - %.2fi\\n), Id(real_part), Id(imaginary_part), Id(real_part), Id(imaginary_part))])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printf, StringLit(The factorial of 5 is: %d\\n), FuncCall(factorial, [IntegerLit(5)])), CallStmt(printf, StringLit(The 10th Fibonacci number is: %d\\n), FuncCall(fibonacci, [IntegerLit(10)])), CallStmt(printf, StringLit(The sum of the first 5 terms of the geometric series with a = 1 and r = 2 is: %.2f\\n), FuncCall(geometric_sum, [IntegerLit(1), IntegerLit(2), IntegerLit(5)])), CallStmt(quadratic_roots, IntegerLit(1), UnExpr(-, IntegerLit(5)), IntegerLit(6))]))
])""" 
        self.assertTrue(TestAST.test(input, expect, 135))
    def test_case_136(self):
        """Testcase 136 """
        input =	"""a: integer = 2;
                    b: integer = 5;
                    c: float = 3.14159;

                    func1: function auto(x: integer, y: integer) {
                        z: integer;
                        z = (x + y) * (x - y);
                        return z;
                    }

                    func2: function auto(x: float, y: float, z: float) {
                        a: float;
                        b: float;
                        c: float;
                        a = x * y * z;
                        b = x + y + z;
                        c = x / y;
                        return (a + b + c);
                    }

                    main: function void() {
                        result1: integer;
                        result2: float;
                        result1 = func1(a, b);
                        result2 = func2(c, result1, c);
                        if ((result1 > 10) && (result2 < 100)) {
                            printf("Both results are within the desired range.");
                        } else if (result1 > 10) {
                            printf("The first result is within the desired range, but the second is not.");
                        } else if (result2 < 100) {
                            printf("The second result is within the desired range, but the first is not.");
                        } else {
                            printf("Neither result is within the desired range.");
                        }
                        i: integer = 0;
                        while (i < 5) {
                            j: integer = i;
                            while (j < 5) {
                                printf("%d, %d\\n", i, j);
                                j = j + 1;
                            }
                            i = i + 1;
                        }
                    } 
                    """
        expect ="""Program([
	VarDecl(a, IntegerType, IntegerLit(2))
	VarDecl(b, IntegerType, IntegerLit(5))
	VarDecl(c, FloatType, FloatLit(3.14159))
	FuncDecl(func1, AutoType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([VarDecl(z, IntegerType), AssignStmt(Id(z), BinExpr(*, BinExpr(+, Id(x), Id(y)), BinExpr(-, Id(x), Id(y)))), ReturnStmt(Id(z))]))
	FuncDecl(func2, AutoType, [Param(x, FloatType), Param(y, FloatType), Param(z, FloatType)], None, BlockStmt([VarDecl(a, FloatType), VarDecl(b, FloatType), VarDecl(c, FloatType), AssignStmt(Id(a), BinExpr(*, BinExpr(*, Id(x), Id(y)), Id(z))), AssignStmt(Id(b), BinExpr(+, BinExpr(+, Id(x), Id(y)), Id(z))), AssignStmt(Id(c), BinExpr(/, Id(x), Id(y))), ReturnStmt(BinExpr(+, BinExpr(+, Id(a), Id(b)), Id(c)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(result1, IntegerType), VarDecl(result2, FloatType), AssignStmt(Id(result1), FuncCall(func1, [Id(a), Id(b)])), AssignStmt(Id(result2), FuncCall(func2, [Id(c), Id(result1), Id(c)])), IfStmt(BinExpr(&&, BinExpr(>, Id(result1), IntegerLit(10)), BinExpr(<, Id(result2), IntegerLit(100))), BlockStmt([CallStmt(printf, StringLit(Both results are within the desired range.))]), IfStmt(BinExpr(>, Id(result1), IntegerLit(10)), BlockStmt([CallStmt(printf, StringLit(The first result is within the desired range, but the second is not.))]), IfStmt(BinExpr(<, Id(result2), IntegerLit(100)), BlockStmt([CallStmt(printf, StringLit(The second result is within the desired range, but the first is not.))]), BlockStmt([CallStmt(printf, StringLit(Neither result is within the desired range.))])))), VarDecl(i, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(<, Id(i), IntegerLit(5)), BlockStmt([VarDecl(j, IntegerType, Id(i)), WhileStmt(BinExpr(<, Id(j), IntegerLit(5)), BlockStmt([CallStmt(printf, StringLit(%d, %d\\n), Id(i), Id(j)), AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1)))])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])""" 
        self.assertTrue(TestAST.test(input, expect, 136))
    def test_case_137(self):
        """Testcase 137 """
        input =	"""
                func1: function auto(x: integer, y: integer) {
                    z: integer;
                    z = (x + y) * (x - y);
                    return z;
                }

                func2: function auto(x: float, y: float) {
                    z: float;
                    z = x * y;
                    return z;
                }

                main: function void() {
                    result1: integer;
                    result2: float;
                    result1 = func1(a, c);
                    result2 = func2(b, d);
                    printf("The result of func1 is %d\\n", result1);
                    printf("The result of func2 is %.2f\\n", result2);
                    if (result1 % 2 == 0) {
                        printf("The result of func1 is even.\\n");
                    } else {
                        printf("The result of func1 is odd.\\n");
                    }
                    if ((result2 > 5) && (result2 < 10)) {
                        printf("The result of func2 is between 5 and 10.\\n");
                    } else {
                        printf("The result of func2 is not between 5 and 10.\\n");
                    }
                    i: integer = 0;
                    while (i < 5) {
                        j: integer = 0;
                        while (j < 5) {
                            if ((i + j == a) && (i * j == c)) {
                                printf("Found solution: i = %d, j = %d\\n", i, j);
                                break;
                            }
                            j = j + 1;
                        }
                        i = i + 1;
                    }
                }"""
        expect ="""Program([
	FuncDecl(func1, AutoType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([VarDecl(z, IntegerType), AssignStmt(Id(z), BinExpr(*, BinExpr(+, Id(x), Id(y)), BinExpr(-, Id(x), Id(y)))), ReturnStmt(Id(z))]))
	FuncDecl(func2, AutoType, [Param(x, FloatType), Param(y, FloatType)], None, BlockStmt([VarDecl(z, FloatType), AssignStmt(Id(z), BinExpr(*, Id(x), Id(y))), ReturnStmt(Id(z))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(result1, IntegerType), VarDecl(result2, FloatType), AssignStmt(Id(result1), FuncCall(func1, [Id(a), Id(c)])), AssignStmt(Id(result2), FuncCall(func2, [Id(b), Id(d)])), CallStmt(printf, StringLit(The result of func1 is %d\\n), Id(result1)), CallStmt(printf, StringLit(The result of func2 is %.2f\\n), Id(result2)), IfStmt(BinExpr(==, BinExpr(%, Id(result1), IntegerLit(2)), IntegerLit(0)), BlockStmt([CallStmt(printf, StringLit(The result of func1 is even.\\n))]), BlockStmt([CallStmt(printf, StringLit(The result of func1 is odd.\\n))])), IfStmt(BinExpr(&&, BinExpr(>, Id(result2), IntegerLit(5)), BinExpr(<, Id(result2), IntegerLit(10))), BlockStmt([CallStmt(printf, StringLit(The result of func2 is between 5 and 10.\\n))]), BlockStmt([CallStmt(printf, StringLit(The result of func2 is not between 5 and 10.\\n))])), VarDecl(i, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(<, Id(i), IntegerLit(5)), BlockStmt([VarDecl(j, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(<, Id(j), IntegerLit(5)), BlockStmt([IfStmt(BinExpr(&&, BinExpr(==, BinExpr(+, Id(i), Id(j)), Id(a)), BinExpr(==, BinExpr(*, Id(i), Id(j)), Id(c))), BlockStmt([CallStmt(printf, StringLit(Found solution: i = %d, j = %d\\n), Id(i), Id(j)), BreakStmt()])), AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1)))])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])""" 
        self.assertTrue(TestAST.test(input, expect, 137))
    def test_case_138(self):
        """Testcase 138 """
        input =	"""
                product: function auto(x: integer, y: integer) {
                    return x * y;
                }

                // Define a function to find the product of all numbers in an array
                productArray: function auto(numRows: integer, numCols: integer) {
                    result: integer = 1;
                    for (i = 0, i < numRows, i + 1) {
                        for (j = 0, j < numCols, j + 1) {
                            result = product(result, arr[i] );
                        }
                    }
                    return result;
                }
                bubbleSort: function void( numRows: integer, numCols: integer) {
                        for (i = 0, i < numRows - 1, i + 1) {
                            for (j = 0, j < numCols - i - 1,j + 1) {
                                if (arr[0]  > arr[0] ) {
                                    // Swap elements
                                    for (k = 0, k < numRows, k + 1) {
                                        temp: integer = arr[k] ;
                                        arr[k]  = arr[k] ;
                                        arr[k]  = temp;
                                    }
                                }
                            }
                        }
                    }
                main: function void() {
                    // Define an array of 5 sub-arrays, each with 4 random integers between 1 and 10
                    arr: array [5, 4] of integer;
                    for (i = 0,i < 5, i + 1) {
                        for (j = 0, j < 4,j + 1) {
                            arr[i] = rand(1, 10);
                        }
                    }

                    // Print the array
                    printf("The array is:\\n");
                    for (i = 0, i < 5, i + 1) {
                        for (j = 0, j < 4, j + 1) {
                            printf("%d ", arr[i] );
                        }
                        printf("\\n");
                    }

                    // Find the sum of the second column
                    sum: integer = 0;
                    for (i = 0,i < 5,   i + 1) {
                        sum = sum + arr[i] ;
                    }
                    printf("The sum of the second column is %d.\\n", sum);

                    // Define a function to find the product of two numbers
                    

                    // Find the product of all numbers in the array
                    productAll: integer = productArray(arr, 5, 4);
                    printf("The product of all numbers in the array is %d.\\n", productAll);

                    // Define a function to sort an array in ascending order using bubble sort algorithm
                    

                    // Sort the array in ascending order
                    bubbleSort(arr, 5, 4);

                    // Print the sorted array
                    printf("The sorted array is:\\n");
                    for (i = 0, i < 5, i + 1) {
                        for (j = 0, j < 4,j + 1) {
                            printf("%d ", arr[i] );
                        }
                        printf("\\n");
                    }
                }

            """
        expect ="""Program([
	FuncDecl(product, AutoType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(*, Id(x), Id(y)))]))
	FuncDecl(productArray, AutoType, [Param(numRows, IntegerType), Param(numCols, IntegerType)], None, BlockStmt([VarDecl(result, IntegerType, IntegerLit(1)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(numRows)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(numCols)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(Id(result), FuncCall(product, [Id(result), ArrayCell(arr, [Id(i)])]))]))])), ReturnStmt(Id(result))]))
	FuncDecl(bubbleSort, VoidType, [Param(numRows, IntegerType), Param(numCols, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, Id(numRows), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), BinExpr(-, BinExpr(-, Id(numCols), Id(i)), IntegerLit(1))), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(arr, [IntegerLit(0)]), ArrayCell(arr, [IntegerLit(0)])), BlockStmt([ForStmt(AssignStmt(Id(k), IntegerLit(0)), BinExpr(<, Id(k), Id(numRows)), BinExpr(+, Id(k), IntegerLit(1)), BlockStmt([VarDecl(temp, IntegerType, ArrayCell(arr, [Id(k)])), AssignStmt(ArrayCell(arr, [Id(k)]), ArrayCell(arr, [Id(k)])), AssignStmt(ArrayCell(arr, [Id(k)]), Id(temp))]))]))]))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([5, 4], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(4)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(arr, [Id(i)]), FuncCall(rand, [IntegerLit(1), IntegerLit(10)]))]))])), CallStmt(printf, StringLit(The array is:\\n)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(4)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([CallStmt(printf, StringLit(%d ), ArrayCell(arr, [Id(i)]))])), CallStmt(printf, StringLit(\\n))])), VarDecl(sum, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(arr, [Id(i)])))])), CallStmt(printf, StringLit(The sum of the second column is %d.\\n), Id(sum)), VarDecl(productAll, IntegerType, FuncCall(productArray, [Id(arr), IntegerLit(5), IntegerLit(4)])), CallStmt(printf, StringLit(The product of all numbers in the array is %d.\\n), Id(productAll)), CallStmt(bubbleSort, Id(arr), IntegerLit(5), IntegerLit(4)), CallStmt(printf, StringLit(The sorted array is:\\n)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(4)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([CallStmt(printf, StringLit(%d ), ArrayCell(arr, [Id(i)]))])), CallStmt(printf, StringLit(\\n))]))]))
])""" 
        self.assertTrue(TestAST.test(input, expect, 138))
    def test_case_139(self):
        """Testcase 139 """
        input =	"""sum: integer = 0;
                i: integer = 0;
                count: integer = 0;
                main: function void(){
                    while (count < 50) {
                        if (i % 2 == 0) {
                            sum = sum+ i;
                            count = count+ 1;
                        }
                    i =i+ 1;
                    }

                    print("The sum of the first 50 even numbers is: " , sum);
                }
        """
        expect ="""Program([
	VarDecl(sum, IntegerType, IntegerLit(0))
	VarDecl(i, IntegerType, IntegerLit(0))
	VarDecl(count, IntegerType, IntegerLit(0))
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(count), IntegerLit(50)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), Id(i))), AssignStmt(Id(count), BinExpr(+, Id(count), IntegerLit(1)))])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), CallStmt(print, StringLit(The sum of the first 50 even numbers is: ), Id(sum))]))
])""" 
        self.assertTrue(TestAST.test(input, expect, 139))
    def test_case_140(self):

        input = """a, b: array [3,2] of integer = {1,2,3 }, {1,2,3 };"""
        expect ="""Program([
	VarDecl(a, ArrayType([3, 2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(b, ArrayType([3, 2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
])""" 
        self.assertTrue(TestAST.test(input, expect, 140))
    def test_case_141(self):
        input = """x: string = "abc"; """
        expect = """Program([
	VarDecl(x, StringType, StringLit(abc))
])"""
        self.assertTrue(TestAST.test(input, expect, 141))
    def test_case_142(self):
        input = """x1z: float;"""
        expect = """Program([
	VarDecl(x1z, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 142))
    def test_case_143(self):
        input = """Array: array [3] of string;"""
        expect = """Program([
	VarDecl(Array, ArrayType([3], StringType))
])"""
        self.assertTrue(TestAST.test(input, expect, 143))
    def test_case_144(self):
        input = """x, y: array [1,1] of float = {2}, {"hello"};"""
        expect = """Program([
	VarDecl(x, ArrayType([1, 1], FloatType), ArrayLit([IntegerLit(2)]))
	VarDecl(y, ArrayType([1, 1], FloatType), ArrayLit([StringLit(hello)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 144))
    def test_case_145(self):
        input = """x: float = writeFloat(1.0); a: integer = -1.5;"""
        expect = """Program([
	VarDecl(x, FloatType, FuncCall(writeFloat, [FloatLit(1.0)]))
	VarDecl(a, IntegerType, UnExpr(-, FloatLit(1.5)))
])"""
        self.assertTrue(TestAST.test(input, expect, 145))
    def test_case_146(self):
        input = """lisa: array[2] of integer =  -1 + 2;"""
        expect = """Program([
	VarDecl(lisa, ArrayType([2], IntegerType), BinExpr(+, UnExpr(-, IntegerLit(1)), IntegerLit(2)))
])"""
        self.assertTrue(TestAST.test(input, expect, 146))
    def test_case_147(self):
        input = """_Func: function void (x: integer) {}"""
        expect = """Program([
	FuncDecl(_Func, VoidType, [Param(x, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 147))
    def test_case_148(self):
        input = """func: function string () {
            do {
                
                while( i - 1 == 0)
                {
                    x: integer = 10;
                }
            }
            while ( i  > 100);
        }"""
        expect = """Program([
	FuncDecl(func, StringType, [], None, BlockStmt([DoWhileStmt(BinExpr(>, Id(i), IntegerLit(100)), BlockStmt([WhileStmt(BinExpr(==, BinExpr(-, Id(i), IntegerLit(1)), IntegerLit(0)), BlockStmt([VarDecl(x, IntegerType, IntegerLit(10))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 148))
    def test_case_149(self):
        input = """func: function boolean () {
            break;
             do {
        while (i % 10 == 0) {
             x = 20;
        }
        if (n == 2) {
            return 0;
        } 
    } while (i > 100);
        }"""
        expect = """Program([
	FuncDecl(func, BooleanType, [], None, BlockStmt([BreakStmt(), DoWhileStmt(BinExpr(>, Id(i), IntegerLit(100)), BlockStmt([WhileStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(10)), IntegerLit(0)), BlockStmt([AssignStmt(Id(x), IntegerLit(20))])), IfStmt(BinExpr(==, Id(n), IntegerLit(2)), BlockStmt([ReturnStmt(IntegerLit(0))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 149))
    def test_case_150(self):
        input = """func: function integer () {
            preventDefault();
        }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([CallStmt(preventDefault, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 150))
    def test_case_151(self):
        input = """func: function integer () {
            printFloat("1+1");
        }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([CallStmt(printFloat, StringLit(1+1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 151))
    def test_case_152(self):
        input = """func: function boolean () {
            readBoolean();
        }"""
        expect = """Program([
	FuncDecl(func, BooleanType, [], None, BlockStmt([CallStmt(readBoolean, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 152))
    def test_case_153(self):
        input = """
            integers: array [5] of integer = {1, 2, 3, "a"};
        """
        expect = """Program([
	VarDecl(integers, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), StringLit(a)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 153))
    def test_case_154(self):
        input = """
            calculateExpApproximation: function float(n: integer) {
            result = 1.0;
            term = 1.0;
            for ( i = 1, i <= n, i + 1) {
                term = (1.0 / n);
                result = term;
            }
            return result;}"""
        expect = """Program([
	FuncDecl(calculateExpApproximation, FloatType, [Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(result), FloatLit(1.0)), AssignStmt(Id(term), FloatLit(1.0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(term), BinExpr(/, FloatLit(1.0), Id(n))), AssignStmt(Id(result), Id(term))])), ReturnStmt(Id(result))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 154))
    def test_case_155(self):
        input = """
       
                     sumNumbers: function integer( ) {
                         sum = 0;
                         i = 1;
                        do {
                            sum =  sum +i;
                            i = i + 1;
                        } while (i <= n);
                        return sum;
                    }"""
        expect = """Program([
	FuncDecl(sumNumbers, IntegerType, [], None, BlockStmt([AssignStmt(Id(sum), IntegerLit(0)), AssignStmt(Id(i), IntegerLit(1)), DoWhileStmt(BinExpr(<=, Id(i), Id(n)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), Id(i))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), ReturnStmt(Id(sum))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 155))
    def test_case_156(self):
        input =	"""a: integer = "str";"""
        expect = """Program([
	VarDecl(a, IntegerType, StringLit(str))
])"""
        self.assertTrue(TestAST.test(input, expect, 156))
    def test_case_157(self):
        input =	"""a: array[100] of boolean = a[1];"""
        expect = """Program([
	VarDecl(a, ArrayType([100], BooleanType), ArrayCell(a, [IntegerLit(1)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 157))
    def test_case_158(self):
        input = """romanToInt : function integer (s : string) {
    n = length(s);
    result = 0;
    for (i = 0, i < n, i + 1) {
        if ((i > 0) && (roman[s[i]] > roman[s[i - 1]])) {
            result = result + roman[s[i]] - 2 * roman[s[i - 1]];
        } else {
            result = result + roman[s[i]];
        }
    }
    return result;
}

main: function void () {
    s = "MCMXCIV";
    printInt(romanToInt(s));
}"""
        expect = """Program([
	FuncDecl(romanToInt, IntegerType, [Param(s, StringType)], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(s)])), AssignStmt(Id(result), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(&&, BinExpr(>, Id(i), IntegerLit(0)), BinExpr(>, ArrayCell(roman, [ArrayCell(s, [Id(i)])]), ArrayCell(roman, [ArrayCell(s, [BinExpr(-, Id(i), IntegerLit(1))])]))), BlockStmt([AssignStmt(Id(result), BinExpr(-, BinExpr(+, Id(result), ArrayCell(roman, [ArrayCell(s, [Id(i)])])), BinExpr(*, IntegerLit(2), ArrayCell(roman, [ArrayCell(s, [BinExpr(-, Id(i), IntegerLit(1))])]))))]), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(roman, [ArrayCell(s, [Id(i)])])))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), StringLit(MCMXCIV)), CallStmt(printInt, FuncCall(romanToInt, [Id(s)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 158))
    def test_case_159(self):
        input = """sum : function integer(a: integer, b: integer) {
    return a + b;
}
main: function void() {
    print(sum(1,2));
}"""
        expect = """Program([
	FuncDecl(sum, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(print, FuncCall(sum, [IntegerLit(1), IntegerLit(2)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 159))
    def test_case_160(self):
        input = """factorial: function integer (n: integer) {
    if (n == 0) {
        return 1;
    }
    return n * factorial(n - 1);
}

main: function void () {
    n = 5;
    print(factorial(n));
}"""
        expect = """Program([
	FuncDecl(factorial, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(IntegerLit(1))])), ReturnStmt(BinExpr(*, Id(n), FuncCall(factorial, [BinExpr(-, Id(n), IntegerLit(1))])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(n), IntegerLit(5)), CallStmt(print, FuncCall(factorial, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 160))
    def test_case_161(self):
        input = """contains: function boolean (arr: array [10] of integer, target: integer) {
    for (i = 0, i < 10, i + 1) {
        if (arr[i] == target) {
            return true;
        }
    }
    return false;
}

main: function void () {
    arr = {5, 2, 8, 4, 9, 1, 3, 7, 6, 0};
    if (contains(arr, 4)) {
        printString("The array contains the target value");
    } else {
        printString("The array does not contain the target value");
    }
}"""
        expect = """Program([
	FuncDecl(contains, BooleanType, [Param(arr, ArrayType([10], IntegerType)), Param(target, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(arr, [Id(i)]), Id(target)), BlockStmt([ReturnStmt(BooleanLit(True))]))])), ReturnStmt(BooleanLit(False))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(arr), ArrayLit([IntegerLit(5), IntegerLit(2), IntegerLit(8), IntegerLit(4), IntegerLit(9), IntegerLit(1), IntegerLit(3), IntegerLit(7), IntegerLit(6), IntegerLit(0)])), IfStmt(FuncCall(contains, [Id(arr), IntegerLit(4)]), BlockStmt([CallStmt(printString, StringLit(The array contains the target value))]), BlockStmt([CallStmt(printString, StringLit(The array does not contain the target value))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 161))
    def test_case_162(self):
        input = """foo: function integer () {
            {}
            {}        
        }"""
        expect = """Program([
	FuncDecl(foo, IntegerType, [], None, BlockStmt([BlockStmt([]), BlockStmt([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 162))
    def test_case_163(self):
        input = """oo: function integer () {
            do {
                a: string = "My name is Chinh";
                b: float = "U are U"::"I am Me";
                i=i+1;
            }
            while (i<10);
        }"""
        expect = """Program([
	FuncDecl(oo, IntegerType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(i), IntegerLit(10)), BlockStmt([VarDecl(a, StringType, StringLit(My name is Chinh)), VarDecl(b, FloatType, BinExpr(::, StringLit(U are U), StringLit(I am Me))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 163))
    def test_case_164(self):
        input = """sum2DArray: function integer (arr: array [10, 10] of integer) {
    sum = 0;
    for (i = 0, i < 10, i + 1) {
        for (j = 0, j < 10, j + 1) {
            sum = sum + arr[i, j];
        }
    }
    return sum;
}"""
        expect = """Program([
	FuncDecl(sum2DArray, IntegerType, [Param(arr, ArrayType([10, 10], IntegerType))], None, BlockStmt([AssignStmt(Id(sum), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(10)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(arr, [Id(i), Id(j)])))]))])), ReturnStmt(Id(sum))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 164))
    def test_case_165(self):
        input = """fibonacci: function integer (n: integer) {
    if (n <= 1) {
        return n;
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

main: function void () {
    n = 10;
    result = fibonacci(n);
    printInt(result);
}"""
        expect = """Program([
	FuncDecl(fibonacci, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<=, Id(n), IntegerLit(1)), BlockStmt([ReturnStmt(Id(n))]), BlockStmt([ReturnStmt(BinExpr(+, FuncCall(fibonacci, [BinExpr(-, Id(n), IntegerLit(1))]), FuncCall(fibonacci, [BinExpr(-, Id(n), IntegerLit(2))])))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(n), IntegerLit(10)), AssignStmt(Id(result), FuncCall(fibonacci, [Id(n)])), CallStmt(printInt, Id(result))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 165))
    def test_case_166(self):
        input = """
fibonacci: function integer(n: integer) {
    if (n <= 1) {
        return n;
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

// Main function
main: function void() {

    print("Enter n: ");
    n = readInt();

    print("Fibonacci number at position ", n, " is: ", fibonacci(n));
}"""
        expect = """Program([
	FuncDecl(fibonacci, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<=, Id(n), IntegerLit(1)), BlockStmt([ReturnStmt(Id(n))]), BlockStmt([ReturnStmt(BinExpr(+, FuncCall(fibonacci, [BinExpr(-, Id(n), IntegerLit(1))]), FuncCall(fibonacci, [BinExpr(-, Id(n), IntegerLit(2))])))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(print, StringLit(Enter n: )), AssignStmt(Id(n), FuncCall(readInt, [])), CallStmt(print, StringLit(Fibonacci number at position ), Id(n), StringLit( is: ), FuncCall(fibonacci, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 166))
    def test_case_167(self):
        input = """insertionSort: function void(arr: array[10] of integer) {
    for (i = 1, i < 10, i+1) {
        key = arr[i];
        j = i - 1;
        while ((j >= 0) && (arr[j] > key)) {
            arr[j+1] = arr[j];
            j = j - 1;
        }
        arr[j+1] = key;
    }
}

printArray: function void(arr: array[10] of integer) {
    for (i = 0, i < 10, i+1) {
        printInt(arr[i]);
        print(" ");
    }
    print("\\n");
}

main: function void() {
    arr = {5, 2, 8, 4, 9, 1, 3, 7, 6, 0};
    print("Original array: ");
    printArray(arr);
    insertionSort(arr);
    print("Sorted array: ");
    printArray(arr);
}"""
        expect = """Program([
	FuncDecl(insertionSort, VoidType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(key), ArrayCell(arr, [Id(i)])), AssignStmt(Id(j), BinExpr(-, Id(i), IntegerLit(1))), WhileStmt(BinExpr(&&, BinExpr(>=, Id(j), IntegerLit(0)), BinExpr(>, ArrayCell(arr, [Id(j)]), Id(key))), BlockStmt([AssignStmt(ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))]), ArrayCell(arr, [Id(j)])), AssignStmt(Id(j), BinExpr(-, Id(j), IntegerLit(1)))])), AssignStmt(ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))]), Id(key))]))]))
	FuncDecl(printArray, VoidType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInt, ArrayCell(arr, [Id(i)])), CallStmt(print, StringLit( ))])), CallStmt(print, StringLit(\\n))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(arr), ArrayLit([IntegerLit(5), IntegerLit(2), IntegerLit(8), IntegerLit(4), IntegerLit(9), IntegerLit(1), IntegerLit(3), IntegerLit(7), IntegerLit(6), IntegerLit(0)])), CallStmt(print, StringLit(Original array: )), CallStmt(printArray, Id(arr)), CallStmt(insertionSort, Id(arr)), CallStmt(print, StringLit(Sorted array: )), CallStmt(printArray, Id(arr))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 167))
    def test_case_168(self):
        input = """main: function void() {
            // Declare and initialize variables.
            float_: array [10] of integer;
            fib_nums: array [10] of integer;
            for (i = 0, i < 10, i + 1) {
                fib_nums[i] = fibonacci(i);
            }

            matrix: array [3, 3] of integer;

            // Find the largest Fibonacci number.
            largest_fib: integer = find_largest(fib_nums);

            // Find the row with the largest sum in the matrix.
            largest_sum: integer = 0;
            largest_sum_row: integer = -1;

            // Output the results.
            printf("The largest Fibonacci number is %d.\\n", largest_fib);
            printf("The row with the largest sum in the matrix is row %d, with a sum of %d.\\n", largest_sum_row, largest_sum);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(float_, ArrayType([10], IntegerType)), VarDecl(fib_nums, ArrayType([10], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(fib_nums, [Id(i)]), FuncCall(fibonacci, [Id(i)]))])), VarDecl(matrix, ArrayType([3, 3], IntegerType)), VarDecl(largest_fib, IntegerType, FuncCall(find_largest, [Id(fib_nums)])), VarDecl(largest_sum, IntegerType, IntegerLit(0)), VarDecl(largest_sum_row, IntegerType, UnExpr(-, IntegerLit(1))), CallStmt(printf, StringLit(The largest Fibonacci number is %d.\\n), Id(largest_fib)), CallStmt(printf, StringLit(The row with the largest sum in the matrix is row %d, with a sum of %d.\\n), Id(largest_sum_row), Id(largest_sum))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 168))
    def test_case_169(self):
        input = """swap: function void(a: integer, b: integer) {
    temp = a;
    a = b;
    b = temp;
}

bubbleSort: function void (arr: array [10] of integer) {
    n = 10;
    swapped = true;
    while (swapped) {
        swapped = false;
        for (i = 0, i < n - 1, i + 1) {
            if (arr[i] > arr[i + 1]) {
                swap(arr[i], arr[i + 1]);
                swapped = true;
            }
        }
    }
}

printArray: function void (arr: array [10] of integer) {
    for (i = 0, i < 10, i + 1) {
        printInt(arr[i]);
    }
}

main: function void () {
    arr = {5, 2, 8, 4, 9, 1, 3, 7, 6, 0};
    bubbleSort(arr);
    printArray(arr);
}"""
        expect = """Program([
	FuncDecl(swap, VoidType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([AssignStmt(Id(temp), Id(a)), AssignStmt(Id(a), Id(b)), AssignStmt(Id(b), Id(temp))]))
	FuncDecl(bubbleSort, VoidType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([AssignStmt(Id(n), IntegerLit(10)), AssignStmt(Id(swapped), BooleanLit(True)), WhileStmt(Id(swapped), BlockStmt([AssignStmt(Id(swapped), BooleanLit(False)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(arr, [Id(i)]), ArrayCell(arr, [BinExpr(+, Id(i), IntegerLit(1))])), BlockStmt([CallStmt(swap, ArrayCell(arr, [Id(i)]), ArrayCell(arr, [BinExpr(+, Id(i), IntegerLit(1))])), AssignStmt(Id(swapped), BooleanLit(True))]))]))]))]))
	FuncDecl(printArray, VoidType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInt, ArrayCell(arr, [Id(i)]))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(arr), ArrayLit([IntegerLit(5), IntegerLit(2), IntegerLit(8), IntegerLit(4), IntegerLit(9), IntegerLit(1), IntegerLit(3), IntegerLit(7), IntegerLit(6), IntegerLit(0)])), CallStmt(bubbleSort, Id(arr)), CallStmt(printArray, Id(arr))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 169))
    def test_case_170(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 170))
    def test_case_171(self):
        input = """
         isValid : function boolean (s : string) {
             if (length(s) % 2 != 0) {
                 return false;
             }
             for (i = 0, i < length(s), i + 1) {
                 if (s[i] == "(") {
                     push(s[i]);
                 } else if (s[i] == ")") {
                     if (top() == "(") {
                         pop();
                     } else {
                         return false;
                     }
                 }
             }
             if (isEmpty()) {
                 return true;
             } else {
                 return false;
             }
         }
         main: function void () {
             s = "((()))";
             if (isValid(s)) {
                 printString("s is valid.");
             } else {
                 printString("s is not valid.");
             }
         }
         """
        expect = """Program([
	FuncDecl(isValid, BooleanType, [Param(s, StringType)], None, BlockStmt([IfStmt(BinExpr(!=, BinExpr(%, FuncCall(length, [Id(s)]), IntegerLit(2)), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(False))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(s)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(s, [Id(i)]), StringLit(()), BlockStmt([CallStmt(push, ArrayCell(s, [Id(i)]))]), IfStmt(BinExpr(==, ArrayCell(s, [Id(i)]), StringLit())), BlockStmt([IfStmt(BinExpr(==, FuncCall(top, []), StringLit(()), BlockStmt([CallStmt(pop, )]), BlockStmt([ReturnStmt(BooleanLit(False))]))])))])), IfStmt(FuncCall(isEmpty, []), BlockStmt([ReturnStmt(BooleanLit(True))]), BlockStmt([ReturnStmt(BooleanLit(False))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), StringLit(((())))), IfStmt(FuncCall(isValid, [Id(s)]), BlockStmt([CallStmt(printString, StringLit(s is valid.))]), BlockStmt([CallStmt(printString, StringLit(s is not valid.))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 171))
    def test_case_172(self):
        input = """
         numDecodings : function integer (s : string) {
             if (s == "") {
                 return 0;
             }
             n = length(s);
             dp : array[6] of integer;
             dp[0] = 1;
             dp[1] = 1;
             for (i = 2, i <= n, i + 1) {
                 if (s[i - 1] != "0") {
                     dp[i] = dp[i - 1];
                 }
                 if ((s[i - 2] == "1") || ((s[i - 2] == "2") && (s[i - 1] < "7"))) {
                     dp[i] = dp[i] + dp[i - 2];
                 }
             }
             return dp[n];
         }
         main: function void () {
             s = "226";
             printInt(numDecodings(s));
         }
         """
        expect = """Program([
	FuncDecl(numDecodings, IntegerType, [Param(s, StringType)], None, BlockStmt([IfStmt(BinExpr(==, Id(s), StringLit()), BlockStmt([ReturnStmt(IntegerLit(0))])), AssignStmt(Id(n), FuncCall(length, [Id(s)])), VarDecl(dp, ArrayType([6], IntegerType)), AssignStmt(ArrayCell(dp, [IntegerLit(0)]), IntegerLit(1)), AssignStmt(ArrayCell(dp, [IntegerLit(1)]), IntegerLit(1)), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(s, [BinExpr(-, Id(i), IntegerLit(1))]), StringLit(0)), BlockStmt([AssignStmt(ArrayCell(dp, [Id(i)]), ArrayCell(dp, [BinExpr(-, Id(i), IntegerLit(1))]))])), IfStmt(BinExpr(||, BinExpr(==, ArrayCell(s, [BinExpr(-, Id(i), IntegerLit(2))]), StringLit(1)), BinExpr(&&, BinExpr(==, ArrayCell(s, [BinExpr(-, Id(i), IntegerLit(2))]), StringLit(2)), BinExpr(<, ArrayCell(s, [BinExpr(-, Id(i), IntegerLit(1))]), StringLit(7)))), BlockStmt([AssignStmt(ArrayCell(dp, [Id(i)]), BinExpr(+, ArrayCell(dp, [Id(i)]), ArrayCell(dp, [BinExpr(-, Id(i), IntegerLit(2))])))]))])), ReturnStmt(ArrayCell(dp, [Id(n)]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), StringLit(226)), CallStmt(printInt, FuncCall(numDecodings, [Id(s)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 172))
    def test_case_173(self):
        input = """
         firstNonRepeating : function string (str : string) {
             for (i = 0, i < length(str), i + 1) {
                 found = false;
                 for (j = 0, j < length(str), j + 1) {
                     if ((i != j) && (str[i] == str[j])) {
                         found = true;
                         break;
                     }
                 }
                 if (!found) {
                     return str[i];
                 }
             }
             return "";
         }
         main: function void () {
             str = "Hello World!";
             printStr(firstNonRepeating(str));
         }
         """
        expect = """Program([
	FuncDecl(firstNonRepeating, StringType, [Param(str, StringType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(str)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(found), BooleanLit(False)), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), FuncCall(length, [Id(str)])), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(&&, BinExpr(!=, Id(i), Id(j)), BinExpr(==, ArrayCell(str, [Id(i)]), ArrayCell(str, [Id(j)]))), BlockStmt([AssignStmt(Id(found), BooleanLit(True)), BreakStmt()]))])), IfStmt(UnExpr(!, Id(found)), BlockStmt([ReturnStmt(ArrayCell(str, [Id(i)]))]))])), ReturnStmt(StringLit())]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(str), StringLit(Hello World!)), CallStmt(printStr, FuncCall(firstNonRepeating, [Id(str)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 173))
    def test_case_174(self):
        input = """
         findCelebrity : function integer (n : integer) {
             candidate = 0;
             for (i = 1, i < n, i + 1) {
                 if (knows(candidate, i)) {
                     candidate = i;
                 }
             }
             for (i = 0, i < n, i + 1) {
                 if ((i != candidate) && ((knows(candidate, i)) || (!knows(i, candidate)))) {
                     return -1;
                 }
             }
             return candidate;
         }
         main: function void () {
             n = 2;
             printInt(findCelebrity(n));
         }
         """
        expect = """Program([
	FuncDecl(findCelebrity, IntegerType, [Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(candidate), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(FuncCall(knows, [Id(candidate), Id(i)]), BlockStmt([AssignStmt(Id(candidate), Id(i))]))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(&&, BinExpr(!=, Id(i), Id(candidate)), BinExpr(||, FuncCall(knows, [Id(candidate), Id(i)]), UnExpr(!, FuncCall(knows, [Id(i), Id(candidate)])))), BlockStmt([ReturnStmt(UnExpr(-, IntegerLit(1)))]))])), ReturnStmt(Id(candidate))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(n), IntegerLit(2)), CallStmt(printInt, FuncCall(findCelebrity, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 174))
    def test_case_175(self):
        input = """
                main: function void () {
            if (a > 10) {
                if (b > 10) {
                    printFloat(1.2);
                }
                else {
                    readString();
                }
            }
            else {
                s = "Hello";
                printString(s);
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), IntegerLit(10)), BlockStmt([IfStmt(BinExpr(>, Id(b), IntegerLit(10)), BlockStmt([CallStmt(printFloat, FloatLit(1.2))]), BlockStmt([CallStmt(readString, )]))]), BlockStmt([AssignStmt(Id(s), StringLit(Hello)), CallStmt(printString, Id(s))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 175))
    def test_case_176(self):
        input = """
            factorial: function integer (n: integer) {
                if ((n == 0) || (n==1)) return 1;
                else return n * factorial(n - 1);
            }

            program: function void () {
                a: integer = factorial(5);
                return;
            }
        """
        expect = """Program([
	FuncDecl(factorial, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(==, Id(n), IntegerLit(0)), BinExpr(==, Id(n), IntegerLit(1))), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(factorial, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(program, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, FuncCall(factorial, [IntegerLit(5)])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 176))
    def test_case_177(self):
        input = """
        program: function void () {
            a: array[3] of integer = {1, 2, 3};
            b: array[2,2] of integer = {{1, 2}, {3, 4}};
            c: array[4] of float;
        }
        """
        expect = """Program([
	FuncDecl(program, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])), VarDecl(b, ArrayType([2, 2], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(3), IntegerLit(4)])])), VarDecl(c, ArrayType([4], FloatType))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 177))
    def test_case_178(self):
        input = """
         removeDuplicates : function integer (nums : array[5] of integer) {
             if (length(nums) == 0) {
                 return 0;
             }
             i = 0;
             for (j = 1, j < length(nums), j + 1) {
                 if (nums[j] != nums[i]) {
                     i = i + 1;
                     nums[i] = nums[j];
                 }
             }
             return i + 1;
         }
         main: function void () {
             nums = {1, 1, 2};
             printInt(removeDuplicates(nums));
         }
         """
        expect = """Program([
	FuncDecl(removeDuplicates, IntegerType, [Param(nums, ArrayType([5], IntegerType))], None, BlockStmt([IfStmt(BinExpr(==, FuncCall(length, [Id(nums)]), IntegerLit(0)), BlockStmt([ReturnStmt(IntegerLit(0))])), AssignStmt(Id(i), IntegerLit(0)), ForStmt(AssignStmt(Id(j), IntegerLit(1)), BinExpr(<, Id(j), FuncCall(length, [Id(nums)])), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(nums, [Id(j)]), ArrayCell(nums, [Id(i)])), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), AssignStmt(ArrayCell(nums, [Id(i)]), ArrayCell(nums, [Id(j)]))]))])), ReturnStmt(BinExpr(+, Id(i), IntegerLit(1)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(nums), ArrayLit([IntegerLit(1), IntegerLit(1), IntegerLit(2)])), CallStmt(printInt, FuncCall(removeDuplicates, [Id(nums)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 178))
    def test_case_179(self):
        input = """
         change : function integer (amount : integer, coins : array[4] of integer) {
             dp : array[5] of integer;
             dp[0] = 1;
             for (i = 0, i < length(coins), i + 1) {
                 for (j = coins[i], j <= amount, j + 1) {
                     dp[j] = dp[j] + dp[j - coins[i]];
                 }
             }
             return dp[amount];
         }
         main: function void () {
             amount = 5;
             coins = {1, 2, 5};
             printInt(change(amount, coins));
         }
         """
        expect = """Program([
	FuncDecl(change, IntegerType, [Param(amount, IntegerType), Param(coins, ArrayType([4], IntegerType))], None, BlockStmt([VarDecl(dp, ArrayType([5], IntegerType)), AssignStmt(ArrayCell(dp, [IntegerLit(0)]), IntegerLit(1)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(coins)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), ArrayCell(coins, [Id(i)])), BinExpr(<=, Id(j), Id(amount)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(dp, [Id(j)]), BinExpr(+, ArrayCell(dp, [Id(j)]), ArrayCell(dp, [BinExpr(-, Id(j), ArrayCell(coins, [Id(i)]))])))]))])), ReturnStmt(ArrayCell(dp, [Id(amount)]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(amount), IntegerLit(5)), AssignStmt(Id(coins), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(5)])), CallStmt(printInt, FuncCall(change, [Id(amount), Id(coins)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 179))
    def test_case_180(self):
        input = """
         twoSum : function array[2] of integer (nums : array[4] of integer, target : integer) {
             n = length(nums);
             for (i = 0, i < n, i + 1) {
                 for (j = i + 1, j < n, j + 1) {
                     if (nums[i] + nums[j] == target) {
                         return {i, j};
                     }
                 }
             }
             return {-1, -1};
         }
         main: function void () {
             nums = {2, 7, 11, 15};
             target = 9;
             printInt(twoSum(nums, target));
         }
         """
        expect = """Program([
	FuncDecl(twoSum, ArrayType([2], IntegerType), [Param(nums, ArrayType([4], IntegerType)), Param(target, IntegerType)], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(nums)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), BinExpr(+, Id(i), IntegerLit(1))), BinExpr(<, Id(j), Id(n)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(+, ArrayCell(nums, [Id(i)]), ArrayCell(nums, [Id(j)])), Id(target)), BlockStmt([ReturnStmt(ArrayLit([Id(i), Id(j)]))]))]))])), ReturnStmt(ArrayLit([UnExpr(-, IntegerLit(1)), UnExpr(-, IntegerLit(1))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(nums), ArrayLit([IntegerLit(2), IntegerLit(7), IntegerLit(11), IntegerLit(15)])), AssignStmt(Id(target), IntegerLit(9)), CallStmt(printInt, FuncCall(twoSum, [Id(nums), Id(target)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 180))
    def test_case_181(self):
        input = """
         threeSum : function array[2] of integer (nums : array[6] of integer) {
             n = length(nums);
             sort(nums);
             result : array [2] of integer= {};
             for (i = 0, i < n, i + 1) {
                 if ((i > 0) && (nums[i] == nums[i - 1])) {
                     continue;
                 }
                 target : integer = -nums[i];
                 left : integer = i + 1;
                 right : integer = n - 1;
                 while (left < right) {
                     if ((nums[left] + nums[right]) == target) {
                         result = append(result, {nums[i], nums[left], nums[right]});
                         left = left + 1;
                         while ((left < right) && (nums[left] == nums[left - 1])) {
                             left = left + 1;
                         }
                         right = right - 1;
                         while ((left < right) && (nums[right] == nums[right + 1])) {
                             right = right - 1;
                         }
                     } else {
                         if ((nums[left] + nums[right]) < target) {
                             left = left + 1;
                         } else {
                             right = right - 1;
                         }
                     }
                 }
             }
             return result;
         }
         main: function void () {
             nums = {-1, 0, 1, 2, -1, -4};
             printInt(threeSum(nums));
         }
         """
        expect = """Program([
	FuncDecl(threeSum, ArrayType([2], IntegerType), [Param(nums, ArrayType([6], IntegerType))], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(nums)])), CallStmt(sort, Id(nums)), VarDecl(result, ArrayType([2], IntegerType), ArrayLit([])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(&&, BinExpr(>, Id(i), IntegerLit(0)), BinExpr(==, ArrayCell(nums, [Id(i)]), ArrayCell(nums, [BinExpr(-, Id(i), IntegerLit(1))]))), BlockStmt([ContinueStmt()])), VarDecl(target, IntegerType, UnExpr(-, ArrayCell(nums, [Id(i)]))), VarDecl(left, IntegerType, BinExpr(+, Id(i), IntegerLit(1))), VarDecl(right, IntegerType, BinExpr(-, Id(n), IntegerLit(1))), WhileStmt(BinExpr(<, Id(left), Id(right)), BlockStmt([IfStmt(BinExpr(==, BinExpr(+, ArrayCell(nums, [Id(left)]), ArrayCell(nums, [Id(right)])), Id(target)), BlockStmt([AssignStmt(Id(result), FuncCall(append, [Id(result), ArrayLit([ArrayCell(nums, [Id(i)]), ArrayCell(nums, [Id(left)]), ArrayCell(nums, [Id(right)])])])), AssignStmt(Id(left), BinExpr(+, Id(left), IntegerLit(1))), WhileStmt(BinExpr(&&, BinExpr(<, Id(left), Id(right)), BinExpr(==, ArrayCell(nums, [Id(left)]), ArrayCell(nums, [BinExpr(-, Id(left), IntegerLit(1))]))), BlockStmt([AssignStmt(Id(left), BinExpr(+, Id(left), IntegerLit(1)))])), AssignStmt(Id(right), BinExpr(-, Id(right), IntegerLit(1))), WhileStmt(BinExpr(&&, BinExpr(<, Id(left), Id(right)), BinExpr(==, ArrayCell(nums, [Id(right)]), ArrayCell(nums, [BinExpr(+, Id(right), IntegerLit(1))]))), BlockStmt([AssignStmt(Id(right), BinExpr(-, Id(right), IntegerLit(1)))]))]), BlockStmt([IfStmt(BinExpr(<, BinExpr(+, ArrayCell(nums, [Id(left)]), ArrayCell(nums, [Id(right)])), Id(target)), BlockStmt([AssignStmt(Id(left), BinExpr(+, Id(left), IntegerLit(1)))]), BlockStmt([AssignStmt(Id(right), BinExpr(-, Id(right), IntegerLit(1)))]))]))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(nums), ArrayLit([UnExpr(-, IntegerLit(1)), IntegerLit(0), IntegerLit(1), IntegerLit(2), UnExpr(-, IntegerLit(1)), UnExpr(-, IntegerLit(4))])), CallStmt(printInt, FuncCall(threeSum, [Id(nums)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 181))
    def test_case_182(self):
        input = """
         flatten : function array[10] of integer (arr : array[10] of integer) {
             result : array[10] of integer;
             for (i = 0, i < length(arr), i + 1) {
                 if (typeof(arr[i]) == "array") {
                     result = result + flatten(arr[i]);
                 } else {
                     result = result + arr[i];
                 }
             }
             return result;
         }
         main: function void () {
             arr : array [10] of integer = {1, 2, {3, 4}, 5, 6};
             print(flatten(arr));
         }
         """
        expect = """Program([
	FuncDecl(flatten, ArrayType([10], IntegerType), [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([VarDecl(result, ArrayType([10], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(arr)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, FuncCall(typeof, [ArrayCell(arr, [Id(i)])]), StringLit(array)), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), FuncCall(flatten, [ArrayCell(arr, [Id(i)])])))]), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(arr, [Id(i)])))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([10], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), ArrayLit([IntegerLit(3), IntegerLit(4)]), IntegerLit(5), IntegerLit(6)])), CallStmt(print, FuncCall(flatten, [Id(arr)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 182))
    def test_case_183(self):
        input = """
         topKFrequent : function array[5] of integer (nums : array[5] of integer, k : integer) {
             result : array[5] of integer;
             for (i = 0, i < length(nums), i + 1) {
                 if (nums[i] > k) {
                     result = result + nums[i];
                 }
             }
             return result;
         }
         main: function void () {
             nums : array [5] of integer = {1, 1, 1, 2, 2, 3};
             k : integer = 2;
             print(topKFrequent(nums, k));
         }
         """
        expect = """Program([
	FuncDecl(topKFrequent, ArrayType([5], IntegerType), [Param(nums, ArrayType([5], IntegerType)), Param(k, IntegerType)], None, BlockStmt([VarDecl(result, ArrayType([5], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(nums)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(nums, [Id(i)]), Id(k)), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(nums, [Id(i)])))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(nums, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(1), IntegerLit(1), IntegerLit(2), IntegerLit(2), IntegerLit(3)])), VarDecl(k, IntegerType, IntegerLit(2)), CallStmt(print, FuncCall(topKFrequent, [Id(nums), Id(k)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 183))
    def test_case_184(self):
        input = """
         countWeatherType : function array[5] of integer (weather : array[5] of string, country : array[5] of string) {
             result : array[5] of integer;
             for (i = 0, i < length(weather), i + 1) {
                 if ((weather[i] == "sunny") || (weather[i] == "cloudy")) {
                     result = result + country[i];
                 }
             }
             return result;
         }
         main: function void () {
             weather : array [5] of string = {"sunny", "cloudy", "rainy"};
             country : array [5] of string = {"Vietnam", "Thailand", "Malaysia"};
             print(countWeatherType(weather, country));
         }
         """
        expect = """Program([
	FuncDecl(countWeatherType, ArrayType([5], IntegerType), [Param(weather, ArrayType([5], StringType)), Param(country, ArrayType([5], StringType))], None, BlockStmt([VarDecl(result, ArrayType([5], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(weather)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(||, BinExpr(==, ArrayCell(weather, [Id(i)]), StringLit(sunny)), BinExpr(==, ArrayCell(weather, [Id(i)]), StringLit(cloudy))), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(country, [Id(i)])))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(weather, ArrayType([5], StringType), ArrayLit([StringLit(sunny), StringLit(cloudy), StringLit(rainy)])), VarDecl(country, ArrayType([5], StringType), ArrayLit([StringLit(Vietnam), StringLit(Thailand), StringLit(Malaysia)])), CallStmt(print, FuncCall(countWeatherType, [Id(weather), Id(country)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 184))
    def test_case_185(self):
        input = """
        program: function void (arr: array [10] of integer, low: integer, high: integer) {
            if (low < high) {
                pi = partition(arr, low, high);
                sort(arr, low, pi - 1);
                sort(arr, pi + 1, high);
            }
        }

        partition: function integer (arr: array [10] of integer, low: integer, high: integer) {
            pivot = arr[high];
            i = low - 1;
            for (j = low, j < high, j + 1) {
                if (arr[j] < pivot) {
                    i = i + 1;
                    temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
            temp = arr[i + 1];
            arr[i + 1] = arr[high];
            arr[high] = temp;
            return i + 1;
        }
        """
        expect = """Program([
	FuncDecl(program, VoidType, [Param(arr, ArrayType([10], IntegerType)), Param(low, IntegerType), Param(high, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(low), Id(high)), BlockStmt([AssignStmt(Id(pi), FuncCall(partition, [Id(arr), Id(low), Id(high)])), CallStmt(sort, Id(arr), Id(low), BinExpr(-, Id(pi), IntegerLit(1))), CallStmt(sort, Id(arr), BinExpr(+, Id(pi), IntegerLit(1)), Id(high))]))]))
	FuncDecl(partition, IntegerType, [Param(arr, ArrayType([10], IntegerType)), Param(low, IntegerType), Param(high, IntegerType)], None, BlockStmt([AssignStmt(Id(pivot), ArrayCell(arr, [Id(high)])), AssignStmt(Id(i), BinExpr(-, Id(low), IntegerLit(1))), ForStmt(AssignStmt(Id(j), Id(low)), BinExpr(<, Id(j), Id(high)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, ArrayCell(arr, [Id(j)]), Id(pivot)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), AssignStmt(Id(temp), ArrayCell(arr, [Id(i)])), AssignStmt(ArrayCell(arr, [Id(i)]), ArrayCell(arr, [Id(j)])), AssignStmt(ArrayCell(arr, [Id(j)]), Id(temp))]))])), AssignStmt(Id(temp), ArrayCell(arr, [BinExpr(+, Id(i), IntegerLit(1))])), AssignStmt(ArrayCell(arr, [BinExpr(+, Id(i), IntegerLit(1))]), ArrayCell(arr, [Id(high)])), AssignStmt(ArrayCell(arr, [Id(high)]), Id(temp)), ReturnStmt(BinExpr(+, Id(i), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 185))
    def test_case_186(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 186))
    def test_case_187(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 187))
    def test_case_188(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 188))
    def test_case_189(self):
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 189))
    def test_case_190(self):
        input = """x, y: float = 0, 4_5.e1;"""
        expect = """Program([
	VarDecl(x, FloatType, IntegerLit(0))
	VarDecl(y, FloatType, FloatLit(450.0))
])"""
        self.assertTrue(TestAST.test(input, expect, 190))
    def test_case_191(self):
        input = """x, y, z: array [2] of integer = -1.2e8, {1,2}, true;"""
        expect = """Program([
	VarDecl(x, ArrayType([2], IntegerType), UnExpr(-, FloatLit(120000000.0)))
	VarDecl(y, ArrayType([2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)]))
	VarDecl(z, ArrayType([2], IntegerType), BooleanLit(True))
])"""
        self.assertTrue(TestAST.test(input, expect, 191))
    def test_case_192(self):
        input = """a, b: array[1] of float;"""
        expect = """Program([
	VarDecl(a, ArrayType([1], FloatType))
	VarDecl(b, ArrayType([1], FloatType))
])"""
        self.assertTrue(TestAST.test(input, expect, 192))
    def test_case_193(self):
        input = """java: float = !!a;"""
        expect = """Program([
	VarDecl(java, FloatType, UnExpr(!, UnExpr(!, Id(a))))
])"""
        self.assertTrue(TestAST.test(input, expect, 193))
    def test_case_194(self):
        input = """siuuuuuuuuuuuuuuuu: string = "Ronaldo";"""
        expect ="""Program([
	VarDecl(siuuuuuuuuuuuuuuuu, StringType, StringLit(Ronaldo))
])"""
        self.assertTrue(TestAST.test(input, expect, 194))
    def test_case_195(self):
        input = """Func_1: function string (out t: integer, inherit z: float) inherit zzz {}"""
        expect = """Program([
	FuncDecl(Func_1, StringType, [OutParam(t, IntegerType), InheritParam(z, FloatType)], zzz, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 195))
    def test_case_196(self):
        input = """func: function float () {
            a = 1;
            b = 2;
        }
        """
        expect = """Program([
	FuncDecl(func, FloatType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(1)), AssignStmt(Id(b), IntegerLit(2))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 196))
    def test_case_197(self):
        input = """func: function string () {
             for (i = 0, i < 1, i - 1) 
             {
                break;
             }
        }"""
        expect = """Program([
	FuncDecl(func, StringType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(1)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([BreakStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 197))
    def test_case_198(self):
        input = """func: function void () {
            if (i==1) 
                if (i==2)
                    if (i > 3)
                        if (i>=5)
                            printString("I love you");
        }"""
        expect ="""Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(i), IntegerLit(1)), IfStmt(BinExpr(==, Id(i), IntegerLit(2)), IfStmt(BinExpr(>, Id(i), IntegerLit(3)), IfStmt(BinExpr(>=, Id(i), IntegerLit(5)), CallStmt(printString, StringLit(I love you))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 198))
    def test_case_199(self):
        input = """func: function integer () {
            while (true) {
            for ( i = 0, i < 2, i + 1)
            {
                continue;
            }
            }
        }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ContinueStmt()]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 199))
