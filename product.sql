SELECT products.product_id , products.name , products.uom_id , products.price_per_unit , uom.uom_name
FROM grocery_store.products inner join uom on products.uom_id=uom.uom_id;

insert into products (name , uom_id , price_per_unit) values ("spinach" , '1' , '34.5'); 