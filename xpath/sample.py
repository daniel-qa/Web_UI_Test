
#多條件選取
element = driver.find_element_by_xpath("//a[contains(text(),'qa_test')]/../..//input")
element.click()
#先定位第一個元件，再向上定位兩層父元素，最後使用只選取特定元件(input) 的方式定址

