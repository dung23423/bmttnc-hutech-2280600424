using TrieuXuanDung_2280600424.Models;

namespace TrieuXuanDung_2280600424.Repositories
{
    public interface ICategoryRepository
    {
        IEnumerable<Category> GetAllCategories();
        Category GetCategoryById(int id);
        void Add(Category category);
        void Update(Category category);
        void Delete(int id);
    }
}
