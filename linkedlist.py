class Node:
    def __init__(self, data, next):
        self.data=data
        self.next=next

class linkedlist:
    def __init__(self):
        self.head=None

    def insert_at_begining(self, data):
        node=Node(data, self.head)
        self.head=node

    def print(self):
        if self.head is None:
            print("linkedlist is empty")
            return 

        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)+'-->'
            itr=itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head=Node(data, None)
        
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data, None)

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception('invalid index')
        if index==0:
            self.head=self.head.next

        itr=self.head
        count=0
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                itr=itr.next
            return count
    def insert_at(self, data, index):
        if index<0 or index>self.get_length():
            raise Exception('invalid index')
        if index==0:
            self.insert_at_begining(data)
            return

        itr=self.head
        count=0
        while itr:
            if count==index-1:
                node=Node(data, itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1
            
if __name__ == "__main__":
    ll=linkedlist()
    ll.insert_values(['Apple','Banana','Orange'])
    print("length is :", ll.get_length())
    ll.remove_at(1)
    ll.insert_at(1,'Muksam')
    ll.print()
