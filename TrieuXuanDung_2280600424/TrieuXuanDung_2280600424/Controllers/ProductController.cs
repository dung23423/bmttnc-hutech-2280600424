using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using TrieuXuanDung_2280600424.Models; 
using TrieuXuanDung_2280600424.Repositories;

namespace TrieuXuanDung_2280600424.Controllers
{
    public class ProductController : Controller
    {
        private readonly IProductRepository _productRepository;
        private readonly ICategoryRepository _categoryRepository;

        public ProductController(IProductRepository productRepository, ICategoryRepository categoryRepository)
        {
            _productRepository = productRepository;
            _categoryRepository = categoryRepository;
        }

        public IActionResult Index()
        {
            var products = _productRepository.GetAllProducts();
            return View(products);
        }

        public IActionResult Details(int id)
        {
            var product = _productRepository.GetProductById(id);
            if (product.Id == 0)
            {
                return NotFound();
            }
            return View(product);
        }
    }
}
