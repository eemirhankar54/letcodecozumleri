struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) 
{
	struct ListNode *bas = NULL , *son = NULL;
	int elde = 0;
	
	while(l1 != NULL || l2 != NULL || elde != 0)
	{
		int sayi1 = (l1 != NULL) ? l1 -> val : 0;
		int sayi2 = (l2 != NULL) ? l2 -> val : 0;
		
		int toplam = sayi1 + sayi2 + elde;
		elde = toplam / 10;
		
		
		struct ListNode* yeni = (struct ListNode*)malloc(sizeof(struct ListNode));
		
		yeni -> val = toplam % 10;
		yeni -> next = NULL;
		
		if(bas == NULL)
		{
			bas = son = yeni;
		}
		else
		{
			son -> next = yeni;
			son = yeni;
		}
		
		if(l1 != NULL) l1 = l1 -> next;
		if(l2 != NULL) l2 = l2 -> next;
		
	}
	
	return bas;
    
}