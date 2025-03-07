using System.Collections.Generic;
using TrieuXuanDung_2280600424.Models;

namespace TrieuXuanDung_2280600424.Repositories
{   
    public interface IProductRepository 
    {
        IEnumerable<Product> GetAllProducts();
        Product GetProductById(int id);
        void Add(Product product);
        void Update(Product product);
        void Delete(int id);
    }
}
