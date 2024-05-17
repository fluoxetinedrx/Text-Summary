from summary import Summarizer
from evaluate import Evaluate
def load_model():
    s = Summarizer()
    e = Evaluate()
    return s, e


summarizer, evaluate = load_model()



full_text = """
    Côn đồ khoác áo học trò  Nhiều người dân gần khu vực trường THPT Phan Đình Phùng (Phố Cửa Bắc, HN) chứng kiến cảnh 4 thanh thiếu niên ở độ tuổi học sinh quây đánh một nữ sinh gục ngã xuống vỉa hè. Nạn nhân là Thanh Hoài, học sinh lớp 12. Chuyện xảy ra ngày 5/3.  Bà nội Hoài cho biết, hai ngày sau đó, Hoài luôn ở trong trạng thái hoảng loạn không thể nói chuyện được. Đầu và mặt Hoài bị đánh bằng ống nước nên sưng đau, choáng váng, không ăn được gì và cũng không thể nói được nhiều.   Theo lời kể của Hoài và những người chứng kiến, bọn côn đồ không chỉ đấm đá vào mặt, bụng mà còn đá vào háng và vùng phía dưới, khiến việc vệ sinh hàng ngày rất khó khăn.   Nguyên nhân của sự việc bắt nguồn từ tính sĩ diện hão của một số kẻ 8X thích chơi trội, thích làm đại ca trong thiên hạ. Theo lời kể của những người chứng kiến, ngày 4/3, Hoài và Kiên gặp nhau ở trường và có vài lời qua lại.   Ngay ngày hôm sau, Kiên đã gọi bạn đến đánh Hoài ngay tại cổng trường với lý do "đòi lại danh dự vì hôm qua bị xúc phạm". Điều đáng nói thêm là, hành vi ấy lại diễn ra trước sự chứng kiến của khá nhiều người, trong đó có cả bạn cùng lớp của Hoài.   Không có hành động can ngăn, giúp đỡ. Chỉ có vài tiếng bất bình nho nhỏ đủ mình nghe, Hoài oằn mình chịu trận đòn khủng khiếp ngay trước cổng trường.  Câu chuyện của Hoài chỉ là một trong nhiều vụ bạo lực học đường diễn ra ở các trường THPT, thậm chí các trường THCS.   Chị Thanh, bán hàng ăn trước cổng trường THPT Chu Văn An cho biết: "Chị bán ở đây đã 20 năm trời, thấy bọn nó "xử" nhau suốt ngày ấy mà. Quan tâm cũng không xuể. Chị chỉ để ý xem bọn nó có phá hàng của mình không, đã trả tiền chưa, chứ không thể nhớ nổi là đánh nhau như thế nào, vì chuyện gì được!".   Vũ khí trong những vụ "xử" nhau này là bàn ghế, guốc cao gót, gậy, côn, tuýp nước, thậm chí dao... Đa số đối tượng tham gia đều ở độ tuổi 15-16.   Mạnh, thành viên của một băng chuyên "gây náo nhiệt" ở trường Trương Định đã "giải nghệ", cho biết: "Trường nào cũng có một vài nhân vật cộm cán được gọi là "người cầm trịch", và ai muốn yên thân thì hãy nhớ mặt, nhớ tên những "người cầm trịch" ấy mà tránh cho xa".   Dĩ nhiên, những kẻ thân thiết với những đàn anh, đàn chị như thế thì "được nhờ trăm sự". Có đứa nào dám sờ đến mình là lại gọi hội đến "xử". Có thấy ngứa mắt đứa nào là gọi người đến dằn mặt cảnh cáo.   Với cả một hệ thống có trên có dưới, "xã hội đen nhí" hoạt động như luật rừng. Chỉ một cú điện thoại, ngay lập tức cả hội sẽ có mặt để yểm trợ chiến hữu. Không cần biết lý do gì, ở đâu cũng không quan trọng, chỉ cần được chỉ điểm là đánh luôn.   Kiểu hẹn nhau ra địa điểm riêng "nói chuyện" xem ra ngày càng mất thì giờ. Những cuộc "nói chuyện" được thực hiện ngay trước cổng trường hoặc trong trường theo kiểu phủ đầu, thách thức cả Ban giám hiệu trường học.  Cá biệt có trường hợp hai hội "xử" nhau ở cổng trường cho đến khi có người phải vào cấp cứu mà vẫn chưa tha, ngày hôm sau lại kéo nhau vào bệnh viện gây sự tiếp.  Bác sĩ Phạm Quỳnh Trang, khoa Ngoại bệnh viện Saint Paul cho biết: "Đã có nhiều trường hợp học sinh cấp III phải nhập viện vì là nạn nhân của bạo lực học đường. Mức độ nghiêm trọng của các vết thương là rất khác nhau và cũng không ít trường hợp, chúng tôi phải phẫu thuật ngay lập tức, nếu không sẽ đe doạ đến tính mạng".  "Số nạn nhân không hề giảm so với vài năm trước", bác sĩ Trang nói thêm.    "
"""
summary = summarizer.summarize(full_text)

score = evaluate.content_based(summary[0], full_text)

list_sentence_selected = list(summary[1])
list_sentence_selected = list(map(str, list_sentence_selected))

# văn bản tóm tắt
print(summary[0]) 

print("Những câu quan trọng: {}".format(", ".join(list_sentence_selected)))
print("Giữ lại {:.2f}% nội dung văn bản".format(score*100))