# Nhận dạng thông tin từ CCCD

## How It Works

Như tiêu đề, web chỉ có một nhiệm vụ duy nhất là trích xuất thông tin từ ảnh chụp CCCD

## How To Run

<details><summary><b>Linux and Mac</b></summary>

1. Đảm bảo đã cài đặt `pip3` và `python3`:

    ```sh
    sudo apt install python3 python3-pip
    ```

2. Chúng tôi khuyến nghị sử dụng `virtual env` nhưng nếu bạn không quan tâm lắm thì bỏ qua bước này

3. Update `pip3`:

    ```sh
    pip3 install --upgrade pip
    ```

4. Clone project:

    ```sh
    git clone https://github.com/duchuyvp/ocr-identify-document.git
    cd ocr-identify-document
    ```

5. Giờ thị chạy:

    ```sh
    python3 server.py
    ```

6. Truy cập http://localhost:8080

</details>

<details><summary><b>Docker</b></summary>

Đối với người dùng Windows, thư viện `vietocr` yêu cầu `Visual C++ Redistributable 2015-2022` (không hiểu tại sao) nên để dễ dàng cho người dùng, chúng tôi khuyến nghị sử dụng `Docker` và `Docker Compose`. Việc này khiến người dùng không cần có sẵn `Python` trong máy.
    
Nếu người dùng đã dùng Windows rồi còn cố chấp không sử dụng Docker hay cài đặt một phiên bản Python cao (hoặc thấp) hơn, việc xảy ra một số lỗi vặt thì chúng tôi không biết, cũng đừng post bất cứ cái issue nào.

1. Cài đặt [Docker](<(https://docs.docker.com/desktop/windows/install/)>) và [Docker Compose](<(https://docs.docker.com/compose/install/)>):

2. Clone project:

    ```cmd
    git clone https://github.com/duchuyvp/ocr-identify-document.git
    cd ocr-identify-document
    ```

3. Giờ thị chạy:

    ```cmd
    docker-compose up
    ```

4. Truy cập http://localhost:8080
 </details>
