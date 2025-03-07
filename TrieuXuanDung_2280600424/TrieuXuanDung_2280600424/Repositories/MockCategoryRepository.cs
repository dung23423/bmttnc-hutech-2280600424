using TrieuXuanDung_2280600424.Models;

namespace TrieuXuanDung_2280600424.Repositories
{
    public class MockCategoryRepository : ICategoryRepository
    {
        private readonly List<Category> _categories;

        public MockCategoryRepository()
        {
            _categories = new List<Category>
            {
                new Category { Id = 1, Name = "Electronics", Description = "Electronic devices and accessories" },
                new Category { Id = 2, Name = "Home Goods", Description = "Products for home and living" },
                new Category { Id = 3, Name = "Fashion", Description = "Clothing, shoes, and accessories" },
                new Category { Id = 4, Name = "Sports", Description = "Sports equipment and gear" },
                new Category { Id = 5, Name = "Beauty", Description = "Beauty and personal care products" }
            };
        }
        public IEnumerable<Category> GetAllCategories()
        {
            return _categories;
        }

        public Category GetCategoryById(int id)
        {
            return _categories.FirstOrDefault(c => c.Id == id) ?? new Category();
        }

        public void Add(Category category)
        {
            category.Id = _categories.Max(c => c.Id) + 1;
            _categories.Add(category);
        }

        public void Update(Category category)
        {
            var existingCategory = _categories.FirstOrDefault(c => c.Id == category.Id);
            if (existingCategory != null)
            {
                existingCategory.Name = category.Name;
                existingCategory.Description = category.Description;
            }
        }

        public void Delete(int id)
        {
            var category = _categories.FirstOrDefault(c => c.Id == id);
            if (category != null)
            {
                _categories.Remove(category);
            }
        }
    }
}


