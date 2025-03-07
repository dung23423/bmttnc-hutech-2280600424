﻿using System.ComponentModel.DataAnnotations;

namespace TrieuXuanDung_2280600424.Models
{
    public class Category
    {
        public int Id { get; set; }

        [Required]
        [StringLength(50)]
        public string Name { get; set; } = string.Empty;

        [StringLength(200)]
        public string? Description { get; set; }

        public ICollection<Product>? Products { get; set; }
    }
}
