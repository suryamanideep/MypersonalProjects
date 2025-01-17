
//Name:Shailaja Ganorkar
//ID: 101746162
//Assignment 1

#include<opencv2/core.hpp>
#include<opencv2/highgui.hpp>
#include<opencv2/imgproc.hpp>
#include<iostream>

using namespace cv;
using namespace std;

char girlImages[50], girlMaskImages[50], dinosaur[50], dinousaurMaskImages[50];
Mat src[13]; Mat dinoSrc[13]; Mat girlMaskSrc[13]; Mat dinoMaskSrc[50];
Mat bgImg = imread("C:\\Users\\manid\\OneDrive\\Desktop\\codes\\interactivemedia\\Assignment1\\inputs\\bg_scene.jpg");
Mat bgImgCopy, finalImg;

void LoadImages()
{
    int i = 0;
    bgImg.copyTo(bgImgCopy);

    while (1)
    {
        imshow("window", bgImg);

#pragma region  === Display Girl Images ===

        if (i < 10)
            sprintf_s(girlImages, "C:\\Users\\manid\\OneDrive\\Desktop\\codes\\interactivemedia\\Assignment1\\inputs\\girl\\girl0%d.jpg", i);
        else
            sprintf_s(girlImages, "C:\\Users\\manid\\OneDrive\\Desktop\\codes\\interactivemedia\\Assignment1\\inputs\\girl\\girl%d.jpg", i);

        src[i] = imread(girlImages, 1);

#pragma endregion

#pragma region  === Display Dinousaur Images ===

        if (i < 10)
            sprintf_s(dinosaur, "C:\\Users\\manid\\OneDrive\\Desktop\\codes\\interactivemedia\\Assignment1\\inputs\\dino\\dino0%d.jpg", i);
        else
            sprintf_s(dinosaur, "C:\\Users\\manid\\OneDrive\\Desktop\\codes\\interactivemedia\\Assignment1\\inputs\\dino\\dino%d.jpg", i);
        dinoSrc[i] = imread(dinosaur, 1);

#pragma endregion

#pragma region  === Display GirlMask Images ===

        if (i < 10)
            sprintf_s(girlMaskImages, "C:\\Users\\manid\\OneDrive\\Desktop\\codes\\interactivemedia\\Assignment1\\inputs\\girlmask\\girl_mask_0%d.bmp", i);
        else
            sprintf_s(girlMaskImages, "C:\\Users\\manid\\OneDrive\\Desktop\\codes\\interactivemedia\\Assignment1\\inputs\\girlmask\\girl_mask_%d.bmp", i);

        girlMaskSrc[i] = imread(girlMaskImages, 0);

#pragma endregion

#pragma region  === Display DinoMask Images ===

        if (i < 10)
            dinoMaskSrc[i] = imread("C:\\Users\\manid\\OneDrive\\Desktop\\codes\\interactivemedia\\Assignment1\\inputs\\dinomask\\dinosaur_mask_0" + to_string(i) + ".bmp", 0);
        else
            dinoMaskSrc[i] = imread("C:\\Users\\manid\\OneDrive\\Desktop\\codes\\interactivemedia\\Assignment1\\inputs\\dinomask\\dinosaur_mask_" + to_string(i) + ".bmp", 0);


#pragma endregion

        if (i > 12)
            break;
        else
            i++;
    }
}

void PositionObjectsOnBg(char moveObject = NULL)
{
    int x = bgImg.cols / 1.60; int y = bgImg.rows / 1.65;
    int x1 = bgImg.cols / 2;
    int offsetX = bgImg.cols * 0.15;

    bgImg.copyTo(finalImg);
    while ((true))
    {
        for (int i = 0; i < 13; i++)
        {
            //concat remaining & offset img
            hconcat(finalImg(Range(0, bgImg.rows - 1), Range(offsetX - 1, bgImg.cols - 1)),
                finalImg(Range(0, bgImg.rows - 1), Range(0, offsetX - 1)), finalImg);

            finalImg.copyTo(bgImgCopy);

            int girlX = src[i].cols; int girlY = src[i].rows;
            int dinoX = dinoSrc[i].cols; int dinoY = dinoSrc[i].rows;

            src[i].copyTo(bgImgCopy(Range(y - girlY, y), Range(x - girlX, x)), girlMaskSrc[i]);
            dinoSrc[i].copyTo(bgImgCopy(Range(y - dinoY, y), Range(x1 - dinoX, x1)), dinoMaskSrc[i]);

            imshow("window", bgImgCopy);
            waitKey(70);

        }
    }
}
int main(int argc, char** argv)
{
    while (true)
    {
        LoadImages();
        PositionObjectsOnBg();
    }
}