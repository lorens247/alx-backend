```markdown
# 0x00 - API Pagination

API pagination is crucial for efficiently handling large datasets by breaking them into smaller, manageable chunks. This README covers various pagination strategies and considerations.

## Paginating a Dataset with Simple Page and Page Size Parameters

To paginate a dataset with simple page and page_size parameters, follow these steps:

1. **Define Parameters:** Implement parameters in your API endpoint for specifying the page number (`page`) and the number of items per page (`page_size`).
2. **Query Processing:** Use these parameters to slice the dataset accordingly, retrieving the subset of data corresponding to the requested page.
3. **Response:** Return the paginated data along with metadata such as total number of items, current page number, and page size in the API response.

Example API Endpoint:

```
GET /api/items?page=1&page_size=10
```

## Paginating a Dataset with Hypermedia Metadata

Hypermedia metadata provides additional information about pagination within the API response. Here's how to implement it:

1. **Response Structure:** Include hypermedia links within the API response to navigate between pages, providing URLs for accessing the first, last, next, and previous pages.
2. **Metadata:** Alongside paginated data, include metadata containing information about total number of items, current page number, and page size.

Example Response with Hypermedia Metadata:

```json
{
  "data": [...], // Paginated data
  "meta": {
    "total_items": 1000,
    "page": 1,
    "page_size": 10,
    "links": {
      "first": "/api/items?page=1&page_size=10",
      "last": "/api/items?page=100&page_size=10",
      "next": "/api/items?page=2&page_size=10",
      "prev": null
    }
  }
}
```

## Paginating in a Deletion-Resilient Manner

To paginate in a deletion-resilient manner, ensure consistency and integrity of pagination when items are deleted:

1. **Stable Pagination:** Use stable identifiers or offsets for pagination to maintain consistency even when items are deleted from the dataset.
2. **Handling Deletions:** If an item is deleted while a user is navigating through pages, adjust the pagination to reflect the updated dataset, ensuring a seamless user experience.

Example:

If an item is deleted, adjust pagination offsets accordingly to prevent skipping or duplicating items in subsequent pages.

```