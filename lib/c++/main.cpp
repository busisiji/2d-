#include "KcgMatch.h"

int main(int argc, char **argv)
{

	// 实例化KcgMatch
	// "demo/k"为存储模板的根目录
	// "k"为模板的名字
	kcg_matching::KcgMatch kcg("demo/k", "k");
	// 读取模板图像
	Mat model = imread("m1.bmp");
	// 转灰度
	cvtColor(model, model, COLOR_BGR2GRAY);
	// 指定要制作的模板角度，尺度范围
	kcg_matching::AngleRange ar(-180.f, 180.f, 10.f);
	kcg_matching::ScaleRange sr(0.70f, 1.3f, 0.05f);
	// 开始制作模板
	kcg.MakingTemplates(model, ar, sr, 0, 30.f, 60.f);

	// 加载模板
	cout << "Loading model ......" << endl;
	kcg.LoadModel();
	cout << "Load succeed." << endl;

	// 读取搜索图像
	Mat source = imread("rings_03.png");
	Mat draw_source;
	source.copyTo(draw_source);
	cvtColor(source, source, COLOR_BGR2GRAY);

	Timer timer;
	// 开始匹配
	auto matches =
			kcg.Matching(source, 0.80f, 0.1f, 30.f, 0.9f,
									 kcg_matching::PyramidLevel_2, 2, 12);
	double t = timer.out("=== Match time ===");
	cout << "Final match size: " << matches.size() << endl
			 << endl;

	// 画出匹配结果
	kcg.DrawMatches(draw_source, matches, Scalar(255, 0, 0));

	// 画出匹配时间
	rectangle(draw_source, Rect(Point(0, 0), Point(136, 20)), Scalar(255, 255, 255), -1);
	cv::putText(draw_source,
							"time: " + to_string(t) + "s",
							Point(0, 16), FONT_HERSHEY_PLAIN, 1.f, Scalar(0, 0, 0), 1);

	// 显示结果图像
	namedWindow("draw_source", 0);
	imshow("draw_source", draw_source);
	waitKey(0);
	system("pause");
}