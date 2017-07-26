# class C:
# 	def _nonzero_(self):
# 		return False
# c=C
# print bool(c)
# from decimal import Decimal
# dec=Decimal('.1')
# print dec
# names=('Faye','Leanna','Daylen')
# print names[0:2]
# s='abcdefgh'
# print s[::-1]
# print s[::2]
# print ('Faye','Leanna','Daylen')[-100:100]
# s='abcde'
# i=-1
# for i in range(-1,-len(s),-1):
# 	print s[:i]
# print range(0,5,-1)
# a=range(0,2)
# print a
# s='abcde'
# for i in [None]+range(-1,-len(s),-1):
#  	print  s[:i]
# aString='hello world'
# anotherString='Python is cool!'
# print aString
# print anotherString
# s=str(range(4))
# print s
# aString= aString[:6]+'Python'
# print aString
# aString='different string altogether'
# print aString
# aString='Hello World'
# aString=aString[:3]+aString[4:]
# print aString
# aString=' '
# print aString
# aString='abcd'
# s=len(aString)
# import string
# s=string.uppercase
# print s
# a=string.lowercase
# print a
# b=string.digits
# print b
# c=string.letters
# print c
# import string
# alphas=string.letters+' '
# nums=string.digits
# print 'Welcome to the Identifier Cheaker v1.0'
# print 'Testees must be at least 2 chars long.'
# myInput=raw_input('Identifier to test?')
# if len(myInput)>1:
# 	if myInput[0] not in alphas:
# 		print '''invalid:first symbol must be alphabetic'''
# 	else:
# 		for otherChar in myInput[1:]:
# 			if otherChar not in alphas+nums:
# 				print '''invalid:remaining symbols must be alphanumeric'''
# 				break
# 			else:
# 				print "okay as an identifier"
# foo='Hello' ' ' 'world'
# print foo
# from string import Template
# s=Template('There are ${howmany} ${lang} Quotation Symbols')
# print s.substitute(lang='Python',howmany=3)
# print s.substitute(lang='Python')
# print s.safe_substitute(howmany='3')
# print '\n'
# print r'\n'
# import re
# m=re.search('\\[rtfvn]',r'Hello World!\n')
# if m is not None:m.group()
# a=u'abc'
# print a
# s='foobar'
# for i, t in enumerate(s):
# 	print i, t
# s,t='foa','bar'
# a=zip(s,t)
# print a
# a=list('foo')
# print a
# anotherList=[None]
# anotherList.append("Hi,i'm here")
# print anotherList


# stack=[]

# def pushit():
# 	stack.append(raw_input('Enter New string:').strip())

# def popit():
# 	if len(stack)==0:
# 		print 'Cannot pop from an empty stack'
# 	else:
# 		print 'Remove [',`stack.pop()`,']'

# def viewstack():
# 	print stack

# def showmenu():
# 	pr="""p(U)sh
# 	p(O)p (V)iew
# 	(Q)uit
# 	Enter choice:"""

# 	while True:
# 		while True:
# 			try:
# 				choice==raw_input(pr).strip()[0].lower()
# 			except (EOFError,KeyboardInterrupt,IndexError):
# 				choice='q'

# 			print '\nYou picked:[%s]'%choice
# 			if choice not in 'uovq':
# 				print 'Invalid option,try again'
# 			else:
# 				break

# 		if choice=='q':
# 			break
# 		CMDs[choice]()

# showmenu()

# s=set('cheeseshop')
# for i in s:
# 	print i,
# myTuple=(123,'xyz',45.67)
# i=iter(myTuple)
# print i.next()
# print i.next()
# print i.next()
# print i.next()
# rows=[1,2,3,17]
# def cols:
# 	yield 56
# 	yield 2
# 	yield 1
# import os
# filename=raw_input('Enter file name:')
# fobj=open(filename,'w')
# while True:
# 	aLine=raw_input("Enter a line('.'to quit):")
# 	if aLine != ".":
# 		fobj.write('%s%s'%(aLine,os.linesep))
# 	else:
# 		break
# fobj.close()
# f=open('/tmp/x','w+')
# f.tell()
# import sys
# print 'you entered',len(sys.argv),'arguments...'
# print 'they were:',str(sys.argv)
# import os
# for tmpdir in ('/tmp/',r'c:/tmp'):
# 	if os.path.isdir(tmpdir):
# 		break
# 	else :
# 		print 'no temp directory available'
# 		temdir=''

# if tmpdir:
# 	os.chdir(tmpdir)
# 	cwd=os.getcwd()
# 	print '***current temporary directory:'
# 	print cwd

# 	print '***creating example directory...'
# 	os.mkdir('example')
# 	os.chdir('example')
# 	cwd=os.getcwd()
# 	print '***new working direcory:'
# 	print cwd
# 	print '***original directory listing:'
# 	print os.listdir(cwd)
# 	print '***creating test file...'
# 	fobj=open('test','w')
# 	fobj.write('foo\n')
# 	fobj.write('bar\n')
# 	fobj.close()
# 	print '***updated directory listing:'
# 	print os.listdir(cwd)

# 	print "***tenaming 'test' to 'filetest.txt'"
# 	os.rename('test','filetest.txt')
# 	print '***updated directory listing:'
# 	print os.listdir(cwd)

# 	path=os.path.join(cwd,os.listdir(cwd)[0])
# 	print '***full file pathname'
# 	print path
# 	print '***(pathname,basename)=='
# 	print os.path.split(path)
# 	print '***(filename,extension)=='
# 	print os.path.splitext(os.path.basename(paht))

# 	print '***displaying file contents:'
# 	fobj=open(path)
# 	for eachLine in fobj:
# 		print eachLine,
# 	fobj.close()

# 	print '****deleting test file'
# 	os.remove(path)
# 	print '***updated directory listing:'
# 	print os.listdir(cwd)
# 	os.chdir(os.pardir)
# 	print '***deleting test directory'
# 	os.rmdir('example')
# 	print '***DONE'
# def tupleVarArgs(arg1,arg2='defaultB',*theRest):
# 	'display regular args and non-keyword variable args'
# 	print 'formal arg 1:',arg1
# 	print 'formal arg 2:',arg2
# 	for eachXtrArg in theRest:
# 		print 'another arg:',eachX

# true=lambda :True
# true()
# def add(x,y):return x+y

# from random import randint

# def odd(n):
# 	return n%2

# allNums=[]
# for eachNum in range(9):
# 	allNums.append(randint(1,99))

# print filter(odd,allNums)

# from random import randint
# allNums=[]
# for eachNum in range(9):
# 	allNums.append(randint(1,99))
# print filter(lambda n:n%2,allNums)

# from random import randint
# allNums=[]
# for eachNum in range(9):
# 	allNums.append(randint(1,99))
# print [n for n in allNums if n%2]

# from random import randint as ri
# print [n for n in [ri(1,99)for i in range(9)]if n%2]
# from operator import add,mul
# from functools import partial

# add1=partial(add,1)
# mul100=partial(mul,100)

# from functools import partial
# import Tkinter
# root=Tkinter.Tk()
# MyButton=partial(Tkinter.Button,root,fg='white',bg='blue')
# b1=MyButton(text='Button 1')
# b2=MyButton(text='Button 2')
# qb=MyButton(text='QUIT',bg='red',command=root.quit)
# b1.pack()
# b2.pack()
# qb.pack(fill=Tkinter.X,expand=True)
# root.title('PFAs!')
# root.mainloop()

# def foo():
# 	print "\ncalling foo()..."
# 	bar=200
# 	print "in foo(),bar is",bar
# bar=100
# print "in __main__,bar is",bar
# foo()
# print "\nin __main__,bar is (still)",bar

# is_this_global='xyz'
# def foo():
# 	global is_this_global
# 	this_is_local='abc'
# 	is_this_global='def'
# 	print this_is_local+is_this_global

# foo()
# print is_this_global

# def counter(start_at=0):
# 	count=[start_at]
# 	def incr():
# 		count[0]+=1
# 		return count[0]
# 	return incr

# def procl():
# 	j,k=3,4
# 	print "j==%d and k==%d"%(j,k)
# 	k=5

# def proc2():
# 	j=6
# 	procl()
# 	print "j==%d and k==%d"%(j,k)

# k=7

# procl()
# print "j==%d and k==%d"%(j,k)

# j=8
# proc2()
# print "j==%d and k==%d"%(j,k)

# from random import randint
# def randGen(aList):
# 	while len(aList)>0:
# 		yield aList.pop(randint(0,len(aList)))

# for item in randGen('rock','paper','scissors'):
# 	print item

# def foo():
# 	pass
# foo._doc_='Oops,forgot to add doc str above!'
# foo.version=0.2

# class MyClass(object):
# 	'MyClass class definition'
# 	myVersion='1.1'
# 	def showMyVersion(self):
# 		print MyClass.myVersion

# print dir(MyClass)
# print MyClass.__dict__

# class C(object):
# 	pass

# print C.__module__

# class C(P):
# 	def __init__(self):
# 		print 'initialized'
# 	def __del__(self):
# 		p.__del__(self)
# 		print 'deleted'

# c1=C()

# class InstCt(object):
# 	count=0

# 	def __init__(self):
# 		InstCt.count+=1

# 	def __del__(self):
# 		InstCt.count-=1

# 	def howMany(self):
# 		return InstCt.count

# a=InstCt()
# b=InstCt()

# print b.howMany()
# print a.howMany()

# class TestStaticMethod:
# 	def foo():
# 		print 'calling static method foo()'
# 	foo=staticmethod(foo)

# class TestClassMethod:
# 	def foo(cls):
# 		print 'calling class method foo()'
# 		print 'foo() is part of class:',cls._name_

# 	foo=classmethod(foo)

# TestStaticMethod.foo()
# tsm=TestStaticMethod()
# tsm.foo()

# class Parent(object):
# 	def parentMethod(self):
# 		print 'calling parent method'

# class Child(Parent):
# 	def childMethod(self):
# 		print 'calling child method'

# p=Parent()
# p.parentMethod()
# c=Child()
# c.childMethod()
# class P(object):
# 	pass
# class C(P):
# 	pass

# c=C()
# print c.__class__
# p=P()
# print p.__class__

# class P(object):
# 	'P class'
# 	def __init__(self):
# 		print 'created an instance of',self.__class__.__name__

# class C(P):
# 	pass

# p=P()
# c=C()

# print p.__class__
# print c.__class__
# print P.__bases__
# print C.__bases__

# class P(object):
# 	def foo(self):
# 		print 'Hi,I am P-foo()'

# p=P()
# p.foo()

# class C(P):
# 	def foo(self):
# 		print 'Hi,I am C-foo'

# c=C()
# c.foo()

# p.foo()

# class C(P):
# 	def foo(self):
# 		P.foo(self)
# 		print 'Hi,I am C-foo'

# c=C()
# c.foo()

# class C(P):
# 	def foo(self):
# 		super(C,self).foo()
# 		print 'Hi,I am C-foo()'

# c=C()
# c.foo()

# class P(object):
# 	def __init__(self):
# 		print "calling P's constructor"

# class C(P):
# 	def __init__(self):
# 		P.__init__(self)
# 		print "calling C's constructor"

# c=C()

# class RoundFloat(float):
# 	def __new__(cls,val):
# 		# return float.__new__(cls,round(val,2))
# 		return super(RoundFloat,cls).__new__(cls,round(val,2))

# class SortedKeyDict(dict):
# 	def keys(self):
# 		# return sorted(super(SortedKeyDict,self).keys())
# 		return sorted(self.keys())

# class P1(object):
# 	def foo(self):
# 		print 'called P1-foo()'
# class P2(object):
# 	def foo(self):
# 		print 'called P2-foo()'

# 	def bar(self):
# 		print 'called P2-bar()'

# class C1(P1,P2):
# 	pass

# class C2(P2,P1):
# 	def bar(self):
# 		print 'called C2-bar()'

# class GC(C1,C2):
# 	pass

# gc=GC()
# gc.foo()
# gc.bar()

# class myClass(object):
# 	def __init__(self):
# 		self.foo=100

# myInst=myClass()
# print hasattr(myInst,'foo')
# print getattr(myInst,'foo')
# getattr(c,'bar','oops!')

# class RoundFloatManual(object):
# 	def __init__(self,val):
# 		assert isinstance(val,float),"Value must be a float!"
# 		self.value=round(val,2)
# 	def __str__(self):
# 		return str(self.value)

# 	__repr__=__str__
# rfm=RoundFloatManual(4.2654564654)
# print rfm
















