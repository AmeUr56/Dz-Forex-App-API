import scrapy


class ExchangesSpider(scrapy.Spider):
    name = "exchanges"
    allowed_domains = ["dinaralgerien.com"]
    start_urls = ["https://dinaralgerien.com/forexalgerie"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                meta={"playwright": True},
                callback=self.parse
            )

    def parse(self, response):
        # Main Div
        main_div = response.xpath("//div[@class='border bg-card shadow bg-gradient-to-r from-black via-gray-900 to-black text-white rounded-lg google-anno-skip']")

        # First Sub Div
        first_sub_div = main_div.xpath(".//div[@class='flex flex-col space-y-1.5 p-6 rounded-t-lg']")

        ## Date
        date = first_sub_div.xpath(".//div[@class='flex items-center justify-center gap-2']/text()").getall()[-1]

        # Second Sub Div
        second_sub_div = main_div.xpath(".//div[@class='p-6 pt-0 bg-gradient-to-r from-black via-gray-900 to-black']")
        
        ## Table
        rows = second_sub_div.xpath(".//table/tbody/tr")
        self.logger.debug(f"Rows: {rows.getall()}")
        
        table_data = []
        for row in rows:
            cols = row.xpath("./td//text()").getall()
            table_data.append(cols)

        yield {
            "date": date,
            "table": table_data
        }

        return date