// Static JavaScript for e-commerce functionality

// Product Listing
const products = [];

function fetchProducts() {
    fetch('/api/products')
        .then(response => response.json())
        .then(data => {
            products.push(...data);
            displayProducts();
        })
        .catch(error => console.error('Error fetching products:', error));
}

function displayProducts() {
    const productContainer = document.getElementById('product-list');
    productContainer.innerHTML = '';
    products.forEach(product => {
        const productElement = document.createElement('div');
        productElement.className = 'product';
        productElement.innerHTML = `<h3>${product.name}</h3><p>${product.description}</p><button onclick=\