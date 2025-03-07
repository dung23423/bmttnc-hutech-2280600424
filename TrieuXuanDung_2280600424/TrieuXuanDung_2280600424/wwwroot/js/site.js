// Add to cart animation
document.addEventListener('DOMContentLoaded', function() {
    const addToCartButtons = document.querySelectorAll('.btn-primary');
    
    addToCartButtons.forEach(button => {
        if (button.textContent.includes('Add to Cart')) {
            button.addEventListener('click', function(e) {
                e.preventDefault();
                
                // Create a small circle element for animation
                const circle = document.createElement('div');
                circle.style.width = '20px';
                circle.style.height = '20px';
                circle.style.backgroundColor = '#4e73df';
                circle.style.borderRadius = '50%';
                circle.style.position = 'absolute';
                circle.style.zIndex = '9999';
                circle.style.opacity = '0.8';
                
                // Position at button
                const rect = button.getBoundingClientRect();
                circle.style.left = (rect.left + rect.width / 2) + 'px';
                circle.style.top = (rect.top + rect.height / 2 + window.scrollY) + 'px';
                
                document.body.appendChild(circle);
                
                // Find cart icon
                const cartIcon = document.querySelector('.fa-shopping-cart');
                const cartRect = cartIcon ? cartIcon.getBoundingClientRect() : null;
                
                if (cartRect) {
                    // Animate to cart
                    circle.style.transition = 'all 0.8s cubic-bezier(0.2, 0.6, 0.3, 1)';
                    circle.style.left = (cartRect.left + cartRect.width / 2) + 'px';
                    circle.style.top = (cartRect.top + cartRect.height / 2 + window.scrollY) + 'px';
                    circle.style.transform = 'scale(0.3)';
                    
                    // Remove after animation
                    setTimeout(() => {
                        circle.remove();
                        
                        // Add shake effect to cart
                        cartIcon.classList.add('fa-shake');
                        setTimeout(() => {
                            cartIcon.classList.remove('fa-shake');
                        }, 500);
                    }, 800);
                } else {
                    // Just make it disappear if cart not found
                    circle.style.transition = 'all 0.5s ease';
                    circle.style.transform = 'scale(0)';
                    setTimeout(() => {
                        circle.remove();
                    }, 500);
                }
                
                // Show success message
                const successMsg = document.createElement('div');
                successMsg.textContent = 'Product added to cart!';
                successMsg.style.position = 'fixed';
                successMsg.style.top = '20px';
                successMsg.style.right = '20px';
                successMsg.style.backgroundColor = '#4e73df';
                successMsg.style.color = 'white';
                successMsg.style.padding = '10px 20px';
                successMsg.style.borderRadius = '5px';
                successMsg.style.zIndex = '9999';
                successMsg.style.boxShadow = '0 2px 10px rgba(0,0,0,0.2)';
                
                document.body.appendChild(successMsg);
                
                // Show animation
                successMsg.style.transition = 'all 0.3s ease';
                successMsg.style.opacity = '0';
                successMsg.style.transform = 'translateY(-20px)';
                
                setTimeout(() => {
                    successMsg.style.opacity = '1';
                    successMsg.style.transform = 'translateY(0)';
                }, 10);
                
                // Hide and remove
                setTimeout(() => {
                    successMsg.style.opacity = '0';
                    successMsg.style.transform = 'translateY(-20px)';
                    setTimeout(() => {
                        successMsg.remove();
                    }, 300);
                }, 3000);
            });
        }
    });
    
    // Product quantity buttons
    const quantityInputs = document.querySelectorAll('.input-group input');
    quantityInputs.forEach(input => {
        const decrementBtn = input.previousElementSi