using System.Collections.Generic;
using System.Linq;
using TrieuXuanDung_2280600424.Models;
namespace TrieuXuanDung_2280600424.Repositories
{
    public class MockProductRepository : IProductRepository
    {
        private readonly List<Product> _products;
        private readonly ICategoryRepository _categoryRepository;

        public MockProductRepository()
        {
            _categoryRepository = new MockCategoryRepository();

            _products = new List<Product>
            {
                new Product
                {
                    Id = 1,
                    Name = "Smartphone X",
                    Description = "Latest smartphone with advanced features",
                    Price = 899.99m,
                    IsNew = true,
                    CategoryId = 1,
                    Category = _categoryRepository.GetCategoryById(1)
                },
                new Product
                {
                    Id = 2,
                    Name = "Coffee Maker",
                    Description = "Premium coffee maker for home use",
                    Price = 129.99m,
                    IsNew = false,
                    CategoryId = 2,
                    Category = _categoryRepository.GetCategoryById(2)
                },
                new Product
                {
                    Id = 3,
                    Name = "Leather Jacket",
                    Description = "Stylish leather jacket for all seasons",
                    Price = 199.99m,
                    IsNew = true,
                    CategoryId = 3,
                    Category = _categoryRepository.GetCategoryById(3)
                },
                new Product
                {
                    Id = 4,
                    Name = "Basketball",
                    Description = "Professional basketball for indoor and outdoor use",
                    Price = 49.99m,
                    IsNew = false,
                    CategoryId = 4,
                    Category = _categoryRepository.GetCategoryById(4)
                },
                new Product
                {
                    Id = 5,
                    Name = "Skincare Set",
                    Description = "Complete skincare routine in one package",
                    Price = 89.99m,
                    IsNew = true,
                    CategoryId = 5,
                    Category = _categoryRepository.GetCategoryById(5)
                },
                new Product
                {
                    Id = 6,
                    Name = "Wireless Earbuds",
                    Description = "High-quality wireless earbuds with noise cancellation",
                    Price = 149.99m,
                    IsNew = false,
                    CategoryId = 1,
                    Category = _categoryRepository.GetCategoryById(1)
                }
            };
        }

        public IEnumerable<Product> GetAllProducts()
        {
            return _products;
        }

        public Product GetProductById(int id)
        {
            return _products.FirstOrDefault(p => p.Id == id) ?? new Product();
        }

        public void Add(Product product)
        {
            product.Id = _products.Max(p => p.Id) + 1;
            if (product.CategoryId.HasValue)
            {
                product.Category = _categoryRepository.GetCategoryById(product.CategoryId.Value);
            }
            _products.Add(product);
        }

        public void Update(Product product)
        {
            var existingProduct = _products.FirstOrDefault(p => p.Id == product.Id);
            if (existingProduct != null)
            {
                existingProduct.Name = product.Name;
                existingProduct.Description = product.Description;
                existingProduct.Price = product.Price;
                existingProduct.ImageUrl = product.ImageUrl;
                existingProduct.IsNew = product.IsNew;
                existingProduct.IsAvailable = product.IsAvailable;
                existingProduct.CategoryId = product.CategoryId;

                if (product.CategoryId.HasValue)
                {
                    existingProduct.Category = _categoryRepository.GetCategoryById(product.CategoryId.Value);
                }
            }
        }

        public void Delete(int id)
        {
            var product = _products.FirstOrDefault(p => p.Id == id);
            if (product != null)
            {
                _products.Remove(product);
            }
        }
    }
}