from owlready2 import *

onto = get_ontology("file://C:/Users/Korpa/OneDrive/Desktop/gadget_recommendations/gadget_recommendations/S22.owx").load()

def recommend_gadget():
    print("Система рекомендаций гаджетов!")
    print("Пожалуйста, укажите ваши предпочтения:")
    brand = input("Предпочитаемый бренд (Apple/Samsung): ").capitalize() or None
    gadget_type = input("Предпочитаемый тип (Phone/Tablet/Laptop): ").capitalize() or None
    price = input("Предпочитаемый ценовой диапазон (Low/High): ").capitalize() or None
    
    recommended_gadget = None
    for gadget in onto.Gadget.instances():
        matches = True
        if brand:
            gadget_brands = [str(b.name) for b in gadget.HadBrand]  
            if brand not in gadget_brands:
                matches = False
        if gadget_type:
            gadget_types = [str(t.name) for t in gadget.HadType]  
            if gadget_type not in gadget_types:
                matches = False
        if price:
            gadget_prices = [str(p.name) for p in gadget.HadPrice]
            if price not in gadget_prices:
                matches = False
        if matches:
            recommended_gadget = gadget.name
            break  
    

    if recommended_gadget:
        print(f"\nНа основе ваших предпочтений я рекомендую гаджет: {recommended_gadget}")
    else:
        print("\nК сожалению, нет гаджетов, соответствующих вашим предпочтениям. Попробуйте другие критерии.")

if __name__ == "__main__":
    recommend_gadget()