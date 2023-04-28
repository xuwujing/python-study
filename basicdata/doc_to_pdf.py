import os
import comtypes.client
from win32com import client as wc
from pdf2image import convert_from_path


def doc2pdf(doc_path, pdf_path):
    """
    基于 Windows 系统的 Word 转 PDF 思路，使用 pywin32 和 comtypes 实现
    :param doc_path: Word 文档路径
    :param pdf_path: PDF 文件输出路径
    """
    # 启动 Word 应用程序
    word = wc.Dispatch('Word.Application')

    # 打开 Word 文档
    doc = word.Documents.Open(doc_path)

    # 转换为 PDF
    doc.SaveAs(pdf_path, FileFormat=17)

    # 关闭 Word 文档和程序
    doc.Close()
    word.Quit()


def ppt2pdf(ppt_path, pdf_path):
    """
    基于 Windows 系统的 PowerPoint 转 PDF 思路，使用 comtypes 实现
    :param ppt_path: PowerPoint 文件路径
    :param pdf_path: PDF 文件输出路径
    """
    # 创建 PowerPoint 应用程序实例
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")

    # 打开 PowerPoint 文件
    ppt = powerpoint.Presentations.Open(ppt_path)

    # 保存为 PDF
    ppt.SaveAs(pdf_path, 32)

    # 关闭 PowerPoint 文件和程序
    ppt.Close()
    powerpoint.Quit()


def docx2pdf(docx_path, pdf_path):
    """
    基于 Python 的 docx2pdf 库来进行 DOCX 转 PDF
    :param docx_path: DOCX 文件路径
    :param pdf_path: PDF 文件输出路径
    """
    import docx2pdf

    docx2pdf.convert(docx_path, pdf_path)


def pptx2pdf(pptx_path, pdf_path):
    """
    基于 pdf2image 和 PIL 库实现的 PPTX 转 PDF
    :param pptx_path: PPTX 文件路径
    :param pdf_path: PDF 文件输出路径
    """
    # PPTX 文件转化为 Image 对象列表
    slide_images = convert_from_path(pptx_path)

    with open(pdf_path, "wb") as pdf_file:
        # 将 Image 对象转化为 PDF 文件
        for slide in slide_images:
            slide.save(pdf_file, "PDF", resolution=100.0)


if __name__ == '__main__':
    # 测试代码
    # Word 转 PDF
    doc_path = "test.doc"
    pdf_path = "test.pdf"
    doc2pdf(doc_path, pdf_path)

    # PowerPoint 转 PDF
    ppt_path = "test.ppt"
    pdf_path = "test.pdf"
    ppt2pdf(ppt_path, pdf_path)

    # DOCX 转 PDF
    docx_path = "test.docx"
    pdf_path = "test.pdf"
    docx2pdf(docx_path, pdf_path)

    # PPTX 转 PDF
    pptx_path = "test.pptx"
    pdf_path = "test.pdf"
    pptx2pdf(pptx_path, pdf_path)
