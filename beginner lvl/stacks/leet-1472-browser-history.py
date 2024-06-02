class BrowserHistory:
    def __init__(self, homepage: str):
        self.currentPage = homepage
        self.backStack = []
        self.forwardStack = []

    def visit(self, url: str) -> None:
        self.backStack.append(self.currentPage)
        self.currentPage = url
        self.forwardStack.clear()

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if not self.backStack:
                break
            self.forwardStack.append(self.currentPage)
            self.currentPage = self.backStack.pop()
        return self.currentPage

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if not self.forwardStack:
                break
            self.backStack.append(self.currentPage)
            self.currentPage = self.forwardStack.pop()
        return self.currentPage


browser = BrowserHistory("default page")
browser.visit('page2')
browser.visit('page3')
browser.visit('page4')
browser.back(3)
browser.forward(1)
print(browser.backStack, "back pages")
print(browser.forwardStack, "forward pages")
print(browser.currentPage)
