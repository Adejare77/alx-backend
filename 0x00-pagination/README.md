# Pagination

Pagination is the process of dividing a large set of data into smaller, manageable chunks or pages. This concept is commonly used in web development and database management to improve the user experience and efficiecy when dealing with large volumes of data
Most endpoints that returns a list of entities at some point will need some pagination. Without pagination, a simple search could return millions or even billions of hits causing extraneous network traffic

## Why Pagination?

1. Improved User Experience: Displaying a large amount of data on a single page can overwhelm users. Pagination breaks the data into a smaller, more digestable chunks, making itn easier to navigate and understand
2. Performance Optimization: Loading a massive dataset at once can slow down performance of a website or application. Pagination helps in loading data incrementally which reduces the initial load time and improves overall performance
3. Reduced Bandwidth Usage: By only fetching and displaying a subset of data at ta time, pagination helps in reducing the amount of data transferred over the network, saving bandwidth and speeding up data retrieval
4. Better Data Organization: Pagination helps in organizing data into logical segments, making it easier for users to find specific information without scrolling through a long list


### Creating Pagination

`sql`
SELECT * FROM items LIMIT {page_size} OFFSET {Offset};

Here, the page_size is the number of items per page, and offset is calculate as: (current_page - 1) * page_size
