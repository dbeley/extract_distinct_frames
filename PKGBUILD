pkgname=extract_distinct_frames-git
pkgver=1.0
pkgrel=1
provides=("${pkgname%-git}")
conflicts=("${pkgname%-git}")
pkgdesc="Extract distinct frames from a video"
arch=('any')
url="https://github.com/dbeley/${pkgname%-git}"
license=('MIT')
depends=(
        'python'
        'python-setuptools'
        'python-tqdm'
        'python-pillow'
        'img2pdf'
        'yt-dlp'
        'ffmpeg'
        )
source=("git+https://github.com/dbeley/${pkgname%-git}")
md5sums=("SKIP")

package() {
  cd "${pkgname%-git}"
  #python setup.py install --prefix=/usr --root="$pkgdir/" --optimize=1 --skip-build
  python setup.py install --prefix=/usr --root="$pkgdir/" --optimize=1 --skip-build
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
