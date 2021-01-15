#3150148 ΡΟΥΣΣΟΣ ΜΙΧΑΗΛ 
#3150037 ΔΟΥΚΑΣ ΑΛΕΞΑΝΔΡΟΣ 
#3150170 ΤΑΣΙΟΠΟΥΛΟΣ ΧΡΗΣΤΟΣ 

class Book:
    numbook=0
    money=0
    def __init__ (self,title,author,quantity,price):
        Book.numbook+=1
        self.title=title
        self.author=author
        self.quantity=quantity
        self.price=price
    def displayBook(self):
        print("Title: ",self.title,", Author: ",self.author,",  Quantity: ",self.quantity,", Price: ",self.price)
    def sellBook(self):
        self.quantity-=1
        Book.money+= self.price

book1=Book("Ο αρχοντας των δαχτυλιδιων","J.R.R. Tolkien",5,11.4)
book2=Book("Εγκλημα και τιμωρια","Φ. Ντοστογιεφσκι",2,13.7)
book3=Book("Η φαρμα των ζωων","G. orwell",4,9.7)
book4=Book("Hobbit","J.R.R. Tolkien",1,8.5)
print("*Menu*")
print("Παρακαλουμε η αναζητηση σας να γινει χωρις τονους.")
print("1.Εμφανιση βιβλιων")
print("2.Αναζητηση Με Βαση Τον Τιτλο Του Βιβλιου")
print("3.Αναζητηση Με Βαση Τον Συγγραφεα")
print("4.Πωληση Ενος Διαθεσιμου Βιβλιου")
print("5.Προμηθεια Ενος Βιβλιου")
print("6.Αλλαγη Τιμης Ενος Βιβλιου")
print("7.Ποσο Ταμειου")
print("8.Εξοδος")
listbook=[book1,book2,book3,book4]
answer=input("Δωστε Την Επιλογη Σας: ")
while(answer!='8'):
    if (int (answer)<8):
        if(answer=="1"):
            for i in listbook:
                if (i.quantity>=1):
                    i.displayBook()
            
        elif(answer=="2"):
            wantedbook=input("Δωστε τον τιτλο του βιβλίου που θελετε: ")
            i=0
            found=False
            while((found!=True)and(len(listbook)>i)):
                
                if ((getattr(listbook[i],'title').upper()==wantedbook.upper())):
                    found=True
                    
                i+=1
                
            if(found):
                
                if(getattr(listbook[i-1],"quantity")>=1):
                    listbook[i-1].displayBook()
                else:
                    print("Το βιβλιο υπαρχει αλλα δεν ειναι διαθεσιμο")
            else:
                print("Το βιβλιο δεν υπαρχει")
                
                
            
        elif(answer=="3"):
            wantedauthor=input("Δωστε τον συγγραφεα που θελετε: ")
            i=0
            found=False
            while((len(listbook)>i)):
                
                if ((getattr(listbook[i],'author').upper()==wantedauthor.upper()) and getattr(listbook[i],"quantity")>=1):
                    found=True
                    listbook[i].displayBook()
                    
                i+=1
                
            if(found==False):
                print("Δεν υπαρχει βιβλιο αυτου του συγγραφεα η δεν ειναι καποιο διαθεσιμο")
            
                
            
        elif(answer=="4"):
            wantedbook=input("Δωστε τον τιτλο του βιβλίου που θελετε: ")
            i=0
            found=False
            while((found!=True)and(len(listbook)>i)):
                
                if ((getattr(listbook[i],'title').upper()==wantedbook.upper())):
                    found=True
                    
                i+=1
                
            if(found):
                
                if(getattr(listbook[i-1],"quantity")>=1):
                    
                    listbook[i-1].sellBook()
                    print("Η ποληση εγινε ! Ο αριθμος τον αντιτυπων ειναι" ,str(getattr(listbook[i-1],"quantity")))
                    listbook[i-1].displayBook()
                    if(getattr(listbook[i-1],"quantity")==0):
                        del listbook[i-1]
                else:
                    print("Το βιβλιο υπαρχει αλλα δεν ειναι διαθεσιμο")
            else:
                print("Το βιβλιο δεν υπαρχει")
            
            
            
        elif(answer=="5"):
            wantedbook=input("Δωστε τον τιτλο του βιβλίου που θελετε: ")
            i=0
            found=False
            while((found!=True)and(len(listbook)>i)):
                
                if ((getattr(listbook[i],'title').upper()==wantedbook.upper())):
                    found=True
                    
                i+=1
                
            if(found and getattr(listbook[i-1],"quantity")>=1):
                print("Το βιβλιο υπαρχει και ειναι διαθεσιμο")
                print("! Ο αριθμος τον αντιτυπων ειναι" ,str(getattr(listbook[i-1],"quantity")))
                answer=input ("αν θελετε να προμηθευτητε και αλλο βιβλιο πατηστε 'ναι' αλλιως πατηστε 'οχι': ")
                if (answer.upper()=="ΝΑΙ"):
                    answer=input("δωστε τον αριθμο τον αντιτυπων που θελετε    ")
                    setattr(listbook[i-1],"quantity",getattr(listbook[i-1],"quantity")+int(answer))
                    print("Η παραγγελια εγινε! Η ποσοτητα των διαθεσιμων βιβλιων ειναι" ,str(getattr(listbook[i-1],"quantity")))
                    
                        
            else:
                print("Το βιβλιο ειτε δεν υπαρχει ειτε δεν ειναι διαθεσιμο οποτε")
                author=input("Δωστε το ονομα του συγγραφεα του: ")
                quantity=input("Δωστε την ποσοτητα που θελετε να προμηθευτειτε: ")
                price=input("Δωστε την τιμη του βιβλιου: ")
                book=Book(wantedbook,author,int(quantity),float(price))
                listbook.append(book)
                
                
                
            
        elif(answer=="6"):
            wantedbook=input("Δωστε τον τιτλο του βιβλίου στο οποιο θελετε να αλλαξετε τιμη: ")
            i=0
            found=False
            while((found!=True)and(len(listbook)>i)):
                
                if ((getattr(listbook[i],'title').upper()==wantedbook.upper())):
                    found=True
                    
                i+=1
                
            if(found and getattr(listbook[i-1],"quantity")>=1):
                answer=input("Δωσε την καινουργια τιμη του βιβλιου: ")
                setattr(listbook[i-1],"price",float(answer))
                print("Η αλλαγη της τιμης εγινε ! Η νεα τιμη ειναι" ,str(getattr(listbook[i-1],"price")))
            else:
                print("Το βιβλιο ειτε δεν υπαρχει ειτε δεν ειναι διαθεσιμο")
            
        elif(answer=="7"):
            print("το ταμειο εχει ",str(Book.money),"ευρω")
            
    else:
        print("Μη αποδεκτη επιλογη.Ξαναδιαλεξε.")
    
    print()
    print("*Menu*")
    print("Παρακαλουμε η αναζητηση σας να γινει χωρις τονους.")
    print("1.Εμφανιση βιβλιων")
    print("2.Αναζητηση Με Βαση Τον Τιτλο Του Βιβλιου")
    print("3.Αναζητηση Με Βαση Τον Συγγραφεα")
    print("4.Πωληση Ενος Διαθεσιμου Βιβλιου")
    print("5.Προμηθεια Ενος Βιβλιου")
    print("6.Αλλαγη Τιμης Ενος Βιβλιου")
    print("7.Ποσο Ταμειου")
    print("8.Εξοδος")
    answer=input("Δωστε Την Επιλογη Σας: ")
