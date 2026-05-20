def merge_orders(web_orders: list, app_orders: list) -> list:
    merged_list = []
    i = 0  
    j = 0  
    
    while i < len(web_orders) and j < len(app_orders):
        if web_orders[i] <= app_orders[j]:
            merged_list.append(web_orders[i])
            i += 1
        else:
            merged_list.append(app_orders[j])
            j += 1
            
    while i < len(web_orders):
        merged_list.append(web_orders[i])
        i += 1
        
    while j < len(app_orders):
        merged_list.append(app_orders[j])
        j += 1
        
    return merged_list

web = [10, 12, 15, 20]
app = [9, 11, 14, 16, 22]
print("\nЗлиття списків замовлень:")
print("Результат:", merge_orders(web, app))