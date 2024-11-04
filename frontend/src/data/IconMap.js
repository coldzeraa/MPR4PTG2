export const IconMap = {
    'dashboard': {
        icon: "fas fa-tachometer-alt",
        label: "Dashboard",
        link: "/dashboard",
    },
    'perimetry': {
        icon: "fas fa-eye",
        label: "Gesichtsfeldmessung",
        link: "/perimetry_info",
        nextLink: "/perimetry",
    },
    'ishihara': {
        icon: "fas fa-eye-dropper",
        label: "Ishihara Test",
        link: "/ishihara_info",
        nextLink: "", // TODO
    },
    'archive': {
        icon: "fas fa-archive",
        label: "Archiv",
        link: "/archive",
    },
    'info': {
        icon: "fas fa-info-circle",
        label: "Info",
        link: "/info",
        nextLinkPath: "",
    },
    'contact': {
        icon: "fas fa-envelope",
        label: "Kontakt",
        link: "/contact",
    }
};