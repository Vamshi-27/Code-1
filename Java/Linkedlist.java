//Singly Linked list

public class Linkedlist
{
    private Node head,tail;
    private int size;

    public Linkedlist()
    {
        this.size=0;
    }

    private class Node
    {
        private int value;
        private Node next;

        public Node(int value)
        {
            this.value=value;
        }
        /*public Node(int value,Node next)
        {
            this.value=value;
            this.next=next;
        }*/
    }

    public void insertFirst(int val)
    {
        Node node = new Node(val);
        node.next=head;
        head=node;

        if(tail==null)
        {
            tail=head;
        }
    }

    public void display()
    {
        Node temp=head;
        while(temp != null)
        {
            System.out.print(temp.value + "->");
            temp=temp.next;
        }
        System.out.print("End");
        System.out.println();
    }

    public void insertend(int val)
    {
        if(tail==null)
        {
            insertFirst(val);
            return;
        }

        Node node = new Node(val);
        tail.next=node;
        tail=node;
        size++;
    }

    public void insert(int val,int index)
    {
        if(index==0)
        {
            insertFirst(val);
            return;
        }
        if(index==size)
        {
            insertend(val);
            return;
        }
    }

    public static void main(String[] args) 
    {
        Linkedlist list = new Linkedlist();
        list.insertFirst(3);
        list.insertFirst(6);
        list.insertFirst(9);
        list.insertFirst(12);

        list.display();
        list.insertend(99);
        list.display();
    }
}
