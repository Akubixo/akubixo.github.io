# Anthony Ranzola — Level Design Portfolio

Static multi-page site, built for GitHub Pages.

## Pages
| File | Page |
|---|---|
| index.html | Home / Work (3 featured projects) |
| ramemoia.html | RAMemoia — capstone, work in progress |
| ire-maiden.html | Ire Maiden |
| arcane-keepers.html | Arcane Keepers |
| about.html | About + resume download |
| contact.html | Contact |

## Publish on GitHub Pages (about 10 minutes)
1. Sign in to GitHub and click **New repository**.
   - For the address `akubixo.github.io`, name the repo exactly `akubixo.github.io`.
   - Make it **Public**.
2. On the new repo page, click **uploading an existing file**. Drag in **everything inside this folder**
   (the .html files plus the `css`, `js`, `images` and `assets` folders), not the folder itself.
   Then click **Commit changes**.
3. Go to **Settings → Pages**. Under *Build and deployment*, set Source to **Deploy from a branch**,
   pick branch **main** and folder **/ (root)**, then click **Save**.
4. After 1–2 minutes the site is live at `https://akubixo.github.io`.
   Open every page and click every link once.

## Custom domain (e.g. anthonyranzola.me)
1. Claim the GitHub Student Developer Pack (education.github.com/pack) and get the free Namecheap `.me` domain,
   or buy a `.com` from any registrar.
2. In GitHub, go to **Settings → Pages → Custom domain**, enter `anthonyranzola.me`, and click **Save**.
3. In the registrar's DNS settings, add:
   - Four **A** records for host `@`: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - One **CNAME** record for host `www` pointing to `akubixo.github.io`
4. Wait for DNS to update (it can take up to a day), then tick **Enforce HTTPS** in Settings → Pages.

## Before you submit
- Run `python check_site.py` in this folder. It checks for broken links, captions, and name/brand
  on every page, and it lists any remaining **TO FILL IN** boxes. Submit only when it reports none.
- WebCourses takes a snapshot at submission. If you change anything afterward, resubmit before the deadline.
  Don't change the site between the deadline and when grades are posted.

## Editing later
Each page is plain HTML. Change text directly in the `.html` files. To add an image, put it in
`images/<project>/` and copy an existing `<figure>` block, including its caption.
